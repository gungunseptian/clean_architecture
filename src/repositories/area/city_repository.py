from .area_repository_base import Base
from src.entities.province_entity import ProvinceEntity

class CityRepository(Base):

    @property
    def name(self):
        return "city"

    def get_query(self,entity):

       return self._result.query(
                self._entity.legacy_id.label("legacy_id"),
                self._entity.name.label("name"),
                ProvinceEntity.legacy_id.label("province_legacy_id")
        )
        
    def get_join(self):
        return self._result.join(ProvinceEntity,  self._entity.province_id==ProvinceEntity.id) 

    def filters(self,filters):

        if filters is not None:

            for v in filters:

                if v == "id":
                    self._result = self._result.filter(self._entity.legacy_id == filters[v] )
                
                if v == "name":
                    self._result = self._result.filter(self._entity.name == filters[v] )
                
                if v == "province_id":
                    self._result = self._result.filter(ProvinceEntity.legacy_id == filters[v] )
                
       
        return self._result

    def parse(self,entityData):

        data = []
        for i in entityData:
            data.append( {"id":i.legacy_id,"name":i.name,"province_id":i.province_legacy_id } )
        return data
    
