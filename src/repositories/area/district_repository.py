from .area_repository_base import Base

class DistrictRepository(Base):

    @property
    def repository_name(self):
        return "district"
    
