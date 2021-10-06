from app.models.categories_model import Category
from flask import jsonify, request, current_app
import psycopg2

def verify_category_exists(id):
    category = Category.query.get(id)

    if not category:
        return {'msg': 'Category not found'}, 404


def get_category_id_by_name_or_create_if_not_exist(name_category):
    category = Category.query.filter_by(name=name_category).first()

    if category:
        return category.id
    
    new_category = Category(name=name_category)
    current_app.db.session.add(new_category)
    current_app.db.session.commit()

    return new_category.id


def create_category():
    data = request.json

    try:
        category = Category(**data)
        session = current_app.db.session

        session.add(category)
        session.commit()

        return jsonify(category), 201

    except psycopg2.errors.UniqueViolation:
        return {'msg': 'Category already exists!'}, 409
    


def update_category_by_id(category_id: int):
    
    if verify_category_exists(category_id):
        return verify_category_exists(category_id)
    
    data = request.json

    Category.query.get(category_id).update(data)
    current_app.db.session.commit()

    category = Category.query.get(category_id)

    return jsonify(category), 200


def delete_category_by_id(category_id: int):
    
    if verify_category_exists(category_id):
        return verify_category_exists(category_id)
    
    category = Category.query.get(category_id)
    session = current_app.db.session

    session.delete(category)
    session.commit()


    return '', 204


def get_all_categories():
    categories_list = Category.query.all()

    return jsonify([{
            "id": category.id,
            "name": category.name,
            "description": category.description,
            "tasks": [{
                "id": task.id,
                "name": task.name,
                "description": task.description,
                "priority": task.eisenhower_classification.type
            } for task in category.tasks]
        } for category in categories_list]), 200