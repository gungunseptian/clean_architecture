from typing import Iterable, Dict, Optional, NamedTuple

class AreaAdapterBase:

    def __init__(self, repository):
        self._use_case = None
        self._filters = None

    def get_list(self):
        
        self._use_case._filters = self._filters
        return self._use_case.get_list()
        
   


