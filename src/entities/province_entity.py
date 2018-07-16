import datetime
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from src.database.sql import Base
from .base_entity import BaseEntity
from src.database.sql import db_session

class ProvinceEntity(Base,BaseEntity):
    __tablename__ = 'bc_province'

    id = Column(String(10), nullable=False, primary_key=True)
    name = Column(String(50), nullable=False)
    legacy_id = Column(String(4), nullable=False)

    # def db_session(self):
    #     return db_session()



   