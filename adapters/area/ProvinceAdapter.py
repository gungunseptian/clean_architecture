from .AreaAdapterBase import AreaAdapterBase
from use_cases.area.get_province.GetProvinceUseCase import GetProvinceUseCase

class ProvinceAdapter(AreaAdapterBase):

    def __init__(self, repository):
        self._use_case = GetProvinceUseCase(repository)
        self._filters = None
