from .area_adapter_base import Base
from src.usecases.area.subdistrict.subdistrict_usecase import Subdistrict as Usecases

class SubdistrictAdapter(Base):

    def __init__(self, repository):
        self._use_case = Usecases(repository)
        self._filters = None
