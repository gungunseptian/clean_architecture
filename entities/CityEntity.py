from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from database.sql import Base
import datetime

class CityEntity(Base):

    __tablename__ = 'bc_city'

    id = Column(String(10), nullable=False, primary_key=True)
    name = Column(String(50), nullable=False)
    legacy_id = Column(String(4), nullable=False)