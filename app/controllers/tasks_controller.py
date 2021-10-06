from app.exc.TasksError import InvalidLevelValue
from app.models.eisenhowers_model import Eisenhower
from app.models.tasks_model import Task
from app.models.tasks_categories_model import TasksCategories
from app.controllers.categories_controller import get_category_id_by_name_or_create_if_not_exist
from flask import jsonify, request, current_app
import psycopg2
import pdb

eisenhower_default = {
    'Do It First': {'importance': 1, 'urgency': 1},
    'Delegate It': {'importance': 1, 'urgency': 2},
    'Schedule It': {'importance': 2, 'urgency': 1},
    'Delete It': {'importance': 2, 'urgency': 2}
}

def get_eisenhower(importance: int, urgency: int):
    if importance == 1 and urgency == 1:
        return Eisenhower.query.filter_by(type='Do It First').one()

    elif importance == 1 and urgency == 2:
        return Eisenhower.query.filter_by(type='Delegate It').one()

    elif importance == 2 and urgency == 1:
        return Eisenhower.query.filter_by(type='Schedule It').one()

    elif importance == 2 and urgency == 2:
        return Eisenhower.query.filter_by(type='Delete It').one()
    
    else:
        return None


def create_relations_task_categories(task_id: int, categories_list: list):
    for category in categories_list:
        category_id = get_category_id_by_name_or_create_if_not_exist(category['name'])

        relation = TasksCategories(task_id=task_id, category_id=category_id)
        session = current_app.db.session

        session.add(relation)
        session.commit()


def create_task():
    data = request.json

    eisenhower = get_eisenhower(data['importance'], data['urgency'])

    if not eisenhower:
        return {'error': {'valid_options': {'importance': [1, 2], 'urgency': [1, 2]},'received_options': {'importance': data['importance'], 'urgency': data['urgency']}}}, 404

    category_list = data.pop('categories')

    try: 

        task = Task(**data, eisenhower_id=eisenhower.id)
        session = current_app.db.session

        session.add(task)
        session.commit()

        create_relations_task_categories(task.id, category_list)

        return jsonify(task.serializer()), 201

    except psycopg2.errors.UniqueViolation:
        return {'msg': 'Task already exists!'}, 409


def verify_task_exists(id):
    task = Task.query.get(id)

    if not task:
        return {'msg': 'task not found'}, 404


def update_task_by_id(task_id: int):

    if verify_task_exists(task_id):
        return verify_task_exists(task_id)

    data = request.json

    task = Task.query.get(task_id)

    new_eisenhower = eisenhower_default[task.eisenhower_classification.type]

    for key in new_eisenhower.keys():
        if key in data.keys():
            new_eisenhower[key] = data[key]

    eisenhower = get_eisenhower(**new_eisenhower)

    if not eisenhower:
        return {'error': {'valid_options': {'importance': [1, 2], 'urgency': [1, 2]},'received_options': {'importance': data['importance'], 'urgency': data['urgency']}}}, 404

    for key, value in data.items():
        setattr(task, key, value)

    task.eisenhower_id = eisenhower.id

    current_app.db.session.add(task)    
    current_app.db.session.commit()

    return {'id': task.id, 'name': task.name, 'description': task.description, 'duration': task.duration, 'eisenhower_classification': task.eisenhower_classification.type}, 200


def delete_task_by_id(task_id: int):

    if verify_task_exists(task_id):
        return verify_task_exists(task_id)
    
    task = Task.query.get(task_id)
    session = current_app.db.session

    session.delete(task)
    session.commit()

    return '', 204
