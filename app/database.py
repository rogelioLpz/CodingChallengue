from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#from models import SolucionReina
from sqlalchemy import Column, Integer, String, Sequence

#Parametros configurados en Docker Postgress
engine = create_engine('postgresql://rlopez:admin@172.28.1.3:5432/cuenca_db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

#Modelo de BD
class SolucionReina(Base):
    __tablename__ = 'SolucionReina'
    id = Column(Integer, Sequence('id'), primary_key=True)
    NumReinas = Column(Integer)
    Solucion = Column(String)
    
    def __init__(self,NumReinas,Solucion):
        self.NumReinas=NumReinas
        self.Solucion=Solucion

def init_db():
	Base.metadata.create_all(bind=engine)
