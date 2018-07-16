from .area_repository_base import Base

class ProvinceRepository(Base):

    @property
    def name(self):
        return "province"
    
    def get_query(self,entity):

        return self._result.query(
                entity.legacy_id.label("legacy_id"),
                entity.name.label("name"),
        )
