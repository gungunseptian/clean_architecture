from src.database.sql import db_session

class BaseEntity():

    def db_session(self):
        
        return db_session



   