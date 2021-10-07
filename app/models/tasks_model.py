from dataclasses import dataclass

from sqlalchemy.orm import relationship


from app.configs.database import db
from sqlalchemy import Column, Integer, String, TEXT, ForeignKey


@dataclass
class Tasks(db.Model):

    id: int
    name: str
    description: str
    duration: str
    eisenhower_classification: str

    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(TEXT)
    duration = Column(Integer)
    importance = Column(Integer)
    urgency = Column(Integer)

    eisenhower_id = Column(Integer, ForeignKey('eisenhowers.id'), nullable=False)

    eisenhower_classification = relationship('Eisenhowers', backref='tasks')

    categories = relationship('Categories', secondary='tasks_categories', backref='tasks')

    def serialize(self, categories_return):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "duration": self.duration,
            "eisenhower_classification": self.eisenhower_classification.type,
            "category": categories_return
        }
