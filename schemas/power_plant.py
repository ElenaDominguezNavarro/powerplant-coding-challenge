from pydantic import BaseModel

from enum import Enum

class PlantType(Enum):
    WIND_TURBINE = "windturbine"
    GAS_FIRED = "gasfired"
    TURBOJET = "turbojet"

# Shared properties
class PowerPlantBase(BaseModel):
    name: str
    type: PlantType
    efficiency: float
    pmin: float
    pmax: float

# Properties to return to client
class PowerPlant(PowerPlantBase):
    name: str
    type: PlantType
    efficiency: float
    pmin: float
    pmax: float

    class Config:
        orm_mode = True