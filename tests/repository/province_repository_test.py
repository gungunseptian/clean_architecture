import pytest
import os, sys
testfolder = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.abspath(os.path.join(testfolder,"../../"))
sys.path.append(project_root)

from src.adapters.area.province_adapter import ProvinceAdapter as Adapter
from src.entities.province_entity import ProvinceEntity as Entity
from src.repositories.area.province_repository import ProvinceRepository as Repo

class TestProvinceRepository:

    def test_get_list(self):
        
        exc = Repo(Entity).get_list()

        assert exc[0]['id'] == "0601"
        assert exc[0]['name'] == "Bali"

    
  



    