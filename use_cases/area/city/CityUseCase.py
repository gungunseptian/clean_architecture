from .CityResponse import CityResponse
# from .GetProvinceRequest import GetProvinceRequest
from use_cases.area.AreaUseCaseBase import AreaUseCaseBase

class CityUseCase(AreaUseCaseBase):
    
    def set_response(self):

        self._response   = CityResponse
    
    


    

    
        