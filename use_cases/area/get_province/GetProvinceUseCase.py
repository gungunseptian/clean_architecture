from .GetProvinceResponse import GetProvinceResponse
from .GetProvinceRequest import GetProvinceRequest
from use_cases.area.AreaUseCaseBase import AreaUseCaseBase

class GetProvinceUseCase(AreaUseCaseBase):

    def set_response(self):

        self._response   = GetProvinceResponse



    

    
        