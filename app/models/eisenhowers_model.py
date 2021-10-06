from sqlalchemy.orm import relationship
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String

@dataclass
class Eisenhower(db.Model):
    type: str

    __tablename__ = 'eisenhowers'

    id = Column(Integer, primary_key=True)
    type = Column(String(100))

    tasks = relationship('Task', backref='eisenhower_classification')

