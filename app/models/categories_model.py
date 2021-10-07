from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import TEXT, Column, Integer, String


@dataclass
class Categories(db.Model):

    id: int
    name: str
    description: str

    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(TEXT)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'tasks': self.tasks
        }
