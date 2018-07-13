class AreaUseCaseBase(object):

    def __init__(self,repository):
        self._repository = repository
        self._response   = None
        self._filters    = None
        
        self.set_response()

    def get_list(self):
   
        self._repository._filters = self._filters
        return self._response(self._repository.get_list()).response()

    def set_response(self):
        pass
    
