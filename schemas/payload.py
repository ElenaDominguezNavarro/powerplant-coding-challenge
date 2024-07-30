from pydantic import BaseModel
from schemas.power_plant import PowerPlant
from typing import List, Dict


# Shared properties
class PayloadBase(BaseModel):
    load: float
    fuels: Dict[str, float] 
    powerplants: List[PowerPlant]

# Properties to return to client
class Payload(PayloadBase):
    load: float
    fuels: Dict[str, float] 
    powerplants: List[PowerPlant]

    class Config:
        orm_mode = True