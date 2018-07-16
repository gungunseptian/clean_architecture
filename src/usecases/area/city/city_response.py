
from src.responses.base import Base

class CityResp(Base):

    def __init__(self,entity):
        self._entity = entity
    
    def response(self):

        data = []
        for i in self._entity:
            
            data.append({"id":i['id'],"name":i['name'],"province_id":i["province_id"] })
            
        return data

    
    