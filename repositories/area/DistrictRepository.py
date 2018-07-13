from .AreaRepositoryAbstractBase import AreaRepositoryAbstractBase

class DistrictRepository(AreaRepositoryAbstractBase):

    @property
    def repository_name(self):
        return "district"
    
