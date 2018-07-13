from .AreaAdapterBase import AreaAdapterBase
from use_cases.area.province.ProvinceUseCase import ProvinceUseCase

class ProvinceAdapter(AreaAdapterBase):

    def __init__(self, repository):
        self._use_case = ProvinceUseCase(repository)
        self._filters = None
