from .area_adapter_base import Base
from src.usecases.area.city.city_usecase import City as Usecases

class CityAdapter(Base):

    def __init__(self, repository):
        self._use_case = Usecases(repository)
        self._filters = None
