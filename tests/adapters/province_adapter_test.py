import pytest
import os, sys
testfolder = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.abspath(os.path.join(testfolder,"../../"))
sys.path.append(project_root)

from src.adapters.area.province_adapter import ProvinceAdapter as Adapter
from mock.entity_mock import Province as Entity
from mock.repository_mock import Province as Repo

class TestProvinceAdapter:

    def test_get_list(self):
        
        exc = Adapter(Repo(Entity)).get_list()

        assert exc[0]['id'] == "0101"
        assert exc[0]['name'] == "Jawa Barat"

    
  



    