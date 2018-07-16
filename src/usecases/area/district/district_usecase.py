from .district_response import DistrictResp
# from .GetProvinceRequest import GetProvinceRequest
from src.usecases.area.area_usecase_base import Base

class District(Base):
    
    def set_response(self):

        self._response   = DistrictResp
    
    


    

    
        