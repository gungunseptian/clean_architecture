
class ResponseBase:

    def __init__(self,entity):
        self._entity = entity

    def response(self):

        return self._entity

    