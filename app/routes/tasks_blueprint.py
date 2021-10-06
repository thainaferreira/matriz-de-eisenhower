from flask import Blueprint
from app.controllers.tasks_controller import create_task, update_task_by_id, delete_task_by_id

bp_task = Blueprint ('task', __name__, url_prefix='/task')

bp_task.post('')(create_task)
bp_task.patch('/<int:task_id>')(update_task_by_id)
bp_task.delete('/<int:task_id>')(delete_task_by_id)