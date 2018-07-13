from .DistrictResponse import DistrictResponse
# from .GetProvinceRequest import GetProvinceRequest
from use_cases.area.AreaUseCaseBase import AreaUseCaseBase

class DistrictUseCase(AreaUseCaseBase):
    
    def set_response(self):

        self._response   = DistrictResponse
    
    


    

    
        