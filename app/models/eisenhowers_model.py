from sqlalchemy.orm import relationship
from app.configs.database import db
from sqlalchemy import Column, Integer, String
from dataclasses import dataclass


@dataclass
class Eisenhowers(db.Model):

    type: str

    __tablename__ = 'eisenhowers'

    id = Column(Integer, primary_key=True)
    type = Column(String(100))
