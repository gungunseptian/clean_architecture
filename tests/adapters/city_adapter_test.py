import pytest
import os, sys
testfolder = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.abspath(os.path.join(testfolder,"../../"))
sys.path.append(project_root)

from src.adapters.area.city_adapter import CityAdapter as Adapter
from mock.repository_mock import City as Repo
from mock.entity_mock import City as Entity

class TestCityAdapter:

    def test_get_list(self):
        
        exc = Adapter(Repo(Entity)).get_list()

        assert exc[0]['id'] == "010101"
        assert exc[0]['name'] == "Bandung"

    
  



    