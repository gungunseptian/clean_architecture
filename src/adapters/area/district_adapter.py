from .area_adapter_base import Base
from src.usecases.area.district.district_usecase import District as Usecases

class DistrictAdapter(Base):

    def __init__(self, repository):
        self._use_case = Usecases(repository)
        self._filters = None
