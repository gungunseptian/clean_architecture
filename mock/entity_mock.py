class Base():

    def __init__(self,Entity):
        self._entity = Entity

class Province(Base):

     def get_list(self):

        return [{"id":"0101","name":"Jawa Barat"}]

class City(Base):

     def get_list(self):

        return [{"id":"010101","name":"Bandung"}]
