from adapters.area.ProvinceAdapter import ProvinceAdapter
from repositories.area.ProvinceRepository import ProvinceRepository
from entities.ProvinceEntity import ProvinceEntity

from adapters.area.CityAdapter import CityAdapter
from repositories.area.CityRepository import CityRepository
from entities.CityEntity import CityEntity

from adapters.area.DistrictAdapter import DistrictAdapter
from repositories.area.DistrictRepository import DistrictRepository
from entities.DistrictEntity import DistrictEntity

exe = ProvinceAdapter(ProvinceRepository(ProvinceEntity))

#exe = CityAdapter(CityRepository(CityEntity))

#exe = DistrictAdapter(DistrictRepository(DistrictEntity))

exe._filters = {"legacy_id":"0101"}
print(exe.get_list())




