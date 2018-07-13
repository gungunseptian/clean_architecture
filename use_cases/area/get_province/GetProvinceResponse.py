from responses.ResponseBase import ResponseBase

class GetProvinceResponse(ResponseBase):

    def __init__(self,entity):
        self._entity = entity

    