from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

HOST="127.0.0.1"
PORT="5432"
DB="logistics"
USERNAME="shipment"
PASSWORD="shipment"

engine = create_engine('postgresql://'+USERNAME+':'+PASSWORD+'@'+HOST+':'+PORT+'/'+DB, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=True,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    Base.metadata.create_all(bind=engine)




