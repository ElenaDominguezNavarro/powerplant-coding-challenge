from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

import schemas


router = APIRouter()

class ResponseItem(BaseModel):
    name: str
    p: float


@router.post("/")
async def production_plan(payload: schemas.Payload):
    try:
        print(f"Load: {payload.load}")
        print("Fuels:")
        for fuel, price in payload.fuels.items():
            print(f"  {fuel}: {price}")
        print("Powerplants:")
        for plant in payload.powerplants:
            print(f"  Name: {plant.name}, Type: {plant.type}, Efficiency: {plant.efficiency}, Pmin: {plant.pmin}, Pmax: {plant.pmax}")
        return payload
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


