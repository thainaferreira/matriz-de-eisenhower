from app.configs.database import db
from app.models.tasks_categories_model import TasksCategories
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship, backref

@dataclass
class Category(db.Model):
    id: int
    name: str
    description: str

    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)

    tasks = relationship('Task', secondary='tasks_categories', backref='categories')
