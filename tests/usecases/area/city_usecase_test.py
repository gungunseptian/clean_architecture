import pytest
import os, sys
testfolder = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.abspath(os.path.join(testfolder,"../../../"))
sys.path.append(project_root)

from src.usecases.area.city.city_usecase import City
from mock.repository_mock import City as CityRepo

class TestCityUseCase:

    def test_get_list(self):
 
        exc = City( CityRepo( None ) ).get_list()
       
        assert exc[0]['id'] == "010101"
        assert exc[0]['name'] == "Bandung"

    