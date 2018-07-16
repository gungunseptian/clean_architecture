from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from src.database.sql import Base
import datetime
from .base_entity import BaseEntity


class DistrictEntity(Base, BaseEntity):

    __tablename__ = 'bc_district'

    id = Column(String(10), nullable=False, primary_key=True)
    name = Column(String(50), nullable=False)