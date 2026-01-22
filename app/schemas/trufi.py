from pydantic import BaseModel
from typing import List, Tuple

class TrufiBase(BaseModel):
    linea: str
    color: str
    coordenadas: List[Tuple[float, float]]

class TrufiResponse(TrufiBase):
    id: int

    class Config:
        from_attributes = True 