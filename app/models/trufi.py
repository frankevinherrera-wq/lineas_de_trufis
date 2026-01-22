from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TrufiModel(Base):
    __tablename__ = "trufis"

    id = Column(Integer, primary_key=True, index=True)
    linea = Column(String, nullable=False)
    color = Column(String)
    # Guardaremos las coordenadas como una lista de listas: [[lat, lng], [lat, lng]]
    coordenadas = Column(JSON, nullable=False)