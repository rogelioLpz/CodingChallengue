from sqlalchemy import Column, Integer, String, Sequence
from database import Base

#Modelo de BD
class SolucionReina(Base):
    __tablename__ = 'SolucionReina'
    id = Column(Integer, Sequence('id'), primary_key=True)
    NumReinas = Column(Integer)
    Solucion = Column(String)
    
    def __init__(self,NumReinas,Solucion):
        self.NumReinas=NumReinas
        self.Solucion=Solucion