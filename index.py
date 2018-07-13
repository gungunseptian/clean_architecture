from adapters.area.ProvinceAdapter import ProvinceAdapter
from repositories.area.ProvinceRepository import ProvinceRepository
from entities.ProvinceEntity import ProvinceEntity

from adapters.area.CityAdapter import CityAdapter
from repositories.area.CityRepository import CityRepository
from entities.CityEntity import CityEntity

exe = ProvinceAdapter(ProvinceRepository(ProvinceEntity))

#exe = CityAdapter(CityRepository(CityEntity))

exe._filters = {"id":1}
print(exe.get_list())




