from .AreaAdapterBase import AreaAdapterBase
from use_cases.area.city.CityUseCase import CityUseCase

class CityAdapter(AreaAdapterBase):

    def __init__(self, repository):
        self._use_case = CityUseCase(repository)
        self._filters = None
