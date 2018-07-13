from .ProvinceResponse import ProvinceResponse
from use_cases.area.AreaUseCaseBase import AreaUseCaseBase

class ProvinceUseCase(AreaUseCaseBase):

    def set_response(self):

        self._response   = ProvinceResponse



    

    
        