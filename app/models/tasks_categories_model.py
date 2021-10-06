from app.configs.database import db
from sqlalchemy import Integer, Column, ForeignKey
from dataclasses import dataclass

@dataclass
class TasksCategories (db.Model): 
    id: int
    task_id: int
    category_id:int 

    __tablename__ = 'tasks_categories'

    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey('tasks.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
