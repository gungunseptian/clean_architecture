from .zipcode_response import ZipcodeResp
from src.usecases.area.area_usecase_base import Base

class Zipcode(Base):

    def set_response(self):

        self._response   = ZipcodeResp



    

    
        