from pydantic import BaseModel


# Shared properties
class PowerPlantBase(BaseModel):
    name: str
    type: str
    efficiency: float
    pmin: float
    pmax: float

# Properties to return to client
class PowerPlant(PowerPlantBase):
    name: str
    type: str
    efficiency: float
    pmin: float
    pmax: float

    class Config:
        orm_mode = True