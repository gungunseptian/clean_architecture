from .AreaRepositoryAbstractBase import AreaRepositoryAbstractBase
class CityRepository(AreaRepositoryAbstractBase):

    @property
    def repository_name(self):
        return "city"
    
