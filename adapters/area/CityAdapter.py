from .AreaAdapterBase import AreaAdapterBase
from use_cases.area.get_city.GetCityUseCase import GetCityUseCase

class CityAdapter(AreaAdapterBase):

    def __init__(self, repository):
        self._use_case = GetCityUseCase(repository)
        self._filters = None
