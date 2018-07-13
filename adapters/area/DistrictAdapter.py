from .AreaAdapterBase import AreaAdapterBase
from use_cases.area.district.DistrictUseCase import DistrictUseCase

class DistrictAdapter(AreaAdapterBase):

    def __init__(self, repository):
        self._use_case = DistrictUseCase(repository)
        self._filters = None
