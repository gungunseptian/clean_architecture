from .AreaRepositoryAbstractBase import AreaRepositoryAbstractBase

class ProvinceRepository(AreaRepositoryAbstractBase):

    @property
    def repository_name(self):
        return "province"
    
