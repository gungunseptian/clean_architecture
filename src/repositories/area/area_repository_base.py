from abc import ABC, abstractmethod, abstractproperty

class Base(ABC):

    def __init__(self,Entity):
        self._entity = Entity
        self._db = self._entity().db_session()
        self._result = None
        self._limit = None
        self._page  = None
        self._filters = None

    @abstractproperty
    def name(self):
        pass

    def get_list(self):
        
        self._result = self._db.query(self._entity)

        if self._limit is not None:
            self._result = self._result.limit(self._limit)

        if self._page is not None:
            self._result = self._result.page(self._page)

        # filters
        self._result = self.filters(self._filters)

        return self.parse(self._result)
    
    def filters(self,filters):

        if filters is not None:

            for v in filters:

                if v == "id":
                    self._result = self._result.filter(self._entity.legacy_id == filters[v] )
                
                if v == "name":
                    self._result = self._result.filter(self._entity.name == filters[v] )
                
        
        return self._result
    
    def parse(self,entityData):

        data = []
        for i in entityData:
            data.append( {"id":i.legacy_id,"name":i.name } )
        return data

    
    # @abstractmethod
    # def get_list(self):
    #     pass

    # @abstractmethod
    # def get_one(self):
    #     pass
    

