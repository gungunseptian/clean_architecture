from .area_repository_base import Base
from src.entities.district_entity import DistrictEntity

class SubdistrictRepository(Base):

    @property
    def name(self):
        return "district"

    def get_query(self,entity):

       return self._result.query(
                self._entity.legacy_id.label("legacy_id"),
                self._entity.name.label("name"),
                DistrictEntity.legacy_id.label("city_legacy_id")
        )
        
    def get_join(self):
        return self._result.join(DistrictEntity,  self._entity.district_id==DistrictEntity.id) 

    def filters(self,filters):
        
        if filters is not None:

            for v in filters:

                if v == "id":
                    self._result = self._result.filter(self._entity.legacy_id == filters[v] )
                
                if v == "name":
                    self._result = self._result.filter(self._entity.name == filters[v] )
                
                if v == "district_id":
                    self._result = self._result.filter(DistrictEntity.legacy_id == filters[v] )
                
        return self._result

    def parse(self,entityData):
    
        data = []
        for i in entityData:
            data.append( {"id":i.legacy_id,"name":i.name,"district_id":i.city_legacy_id } )
        return data
    
    
