
class Base():

    def __init__(self,Entity):
        self._entity = Entity

class Province(Base):

     def get_list(self):

        return [{"id":"0101","name":"Jawa Barat"}]

class City(Base):

     def get_list(self):

        return [{"id":"010101","name":"Bandung"}]

class District(Base):

     def get_list(self):

        return [{"id":"01010101","name":"Cimahi"}]

class Subdistrict(Base):

     def get_list(self):

        return [{"id":"0101010101","name":"Bojong Soang"}]


