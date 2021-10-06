from app.configs.database import db
from app.exc.TasksError import InvalidLevelValue
from app.models.categories_model import Category
from app.models.eisenhowers_model import Eisenhower
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import validates
from sqlalchemy.sql.schema import ForeignKey

@dataclass
class Task(db.Model):
    id: int
    name: str
    description: str
    duration: int
    importance: int
    urgency: int
    eisenhower_id: int

    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    duration = Column(Integer)
    importance = Column(Integer)
    urgency = Column(Integer)
    eisenhower_id = Column(Integer, ForeignKey('eisenhowers.id'), nullable=False)

    def serializer(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "duration": self.duration,
            "eisenhower_classification": self.eisenhower_classification.type,
            "category": [{"name": category.name} for category in self.categories]
        }

    @validates('importance')
    def verify_importance(self, _, importance):
        if importance != 1 and importance != 2:
            raise InvalidLevelValue('Importance level should only be values ​​1 or 2.')

        return importance

    @validates('urgency')
    def verify_urgency(self, _, urgency):
        if urgency != 1 and urgency != 2:
            raise InvalidLevelValue('Urgency level should only be values ​​1 or 2.')

        return urgency