from .area_repository_base import Base

class ProvinceRepository(Base):

    @property
    def name(self):
        return "province"
    
