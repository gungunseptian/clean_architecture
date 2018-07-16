from .area_adapter_base import Base
from src.usecases.area.province.province_usecase import Province as Usecases

class ProvinceAdapter(Base):

    def __init__(self, repository):
        self._use_case = Usecases(repository)
        self._filters = None
