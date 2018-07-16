from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from src.database.sql import Base
import datetime
from .base_entity import BaseEntity


class SubdistrictEntity(Base, BaseEntity):

    __tablename__ = 'bc_subdistrict'

    id = Column(String(10), nullable=False, primary_key=True)
    name = Column(String(50), nullable=False)
    legacy_id = Column(String(6), nullable=False)
    district_id = Column(Integer(), nullable=False)