
from responses.ResponseBase import ResponseBase

class GetCityResponse(ResponseBase):

    def __init__(self,entity):
        self._entity = entity
    
    def response(self):

        data = []
        for i in self._entity:
            
            data.append({"id":i['id'],"name_city":i['name'] })

        return data

    
    