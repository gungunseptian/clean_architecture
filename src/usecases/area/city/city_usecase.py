from .city_response import CityResp
# from .GetProvinceRequest import GetProvinceRequest
from src.usecases.area.area_usecase_base import Base

class City(Base):
    
    def set_response(self):

        self._response   = CityResp