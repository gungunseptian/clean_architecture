import pytest
import os, sys
testfolder = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.abspath(os.path.join(testfolder,"../../../"))
sys.path.append(project_root)

from src.usecases.area.province.province_usecase import Province
from mock.repository_mock import Province as ProvinceRepo

class TestProvinceUseCase:

    def test_get_list(self):
        
        exc = Province( ProvinceRepo( None ) ).get_list()
        assert exc[0]['id'] == "0101"
        assert exc[0]['name'] == "Jawa Barat"

    
  



    