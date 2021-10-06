from flask import Flask
from flask_migrate import Migrate

def init_app(app: Flask):

    from app.models.categories_model import Category
    from app.models.eisenhowers_model import Eisenhower
    from app.models.tasks_model import Task
    from app.models.tasks_categories_model import TasksCategories

    Migrate(app, app.db)