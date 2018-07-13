from .GetCityResponse import GetCityResponse
# from .GetProvinceRequest import GetProvinceRequest
from use_cases.area.AreaUseCaseBase import AreaUseCaseBase

class GetCityUseCase(AreaUseCaseBase):
    
    def set_response(self):

        self._response   = GetCityResponse
    
    


    

    
        