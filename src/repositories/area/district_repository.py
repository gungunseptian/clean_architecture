from .area_repository_base import Base
from src.entities.city_entity import CityEntity

class DistrictRepository(Base):

    @property
    def name(self):
        return "district"

    def get_query(self,entity):

       return self._result.query(
                self._entity.legacy_id.label("legacy_id"),
                self._entity.name.label("name"),
                CityEntity.legacy_id.label("city_legacy_id")
        )
        
    def get_join(self):
        return self._result.join(CityEntity,  self._entity.city_id==CityEntity.id) 

    def filters(self,filters):

        if filters is not None:

            for v in filters:

                if v == "id":
                    self._result = self._result.filter(self._entity.legacy_id == filters[v] )
                
                if v == "name":
                    self._result = self._result.filter(self._entity.name == filters[v] )
                
                if v == "city_id":
                    self._result = self._result.filter(CityEntity.legacy_id == filters[v] )
                
       
        return self._result

    def parse(self,entityData):

        data = []
        for i in entityData:
            data.append( {"id":i.legacy_id,"name":i.name,"city_id":i.city_legacy_id } )
        return data
    
    
