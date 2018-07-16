from .area_repository_base import Base

class CityRepository(Base):

    @property
    def repository_name(self):
        return "city"
    
