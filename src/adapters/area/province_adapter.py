from .area_adapter_base import Base
from src.usecases.area.province.province_usecase import Province

class ProvinceAdapter(Base):

    def __init__(self, repository):
        self._use_case = Province(repository)
        self._filters = None
