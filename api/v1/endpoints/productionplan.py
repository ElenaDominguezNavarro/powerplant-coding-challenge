from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from api.v1.production_service import ProductionService

import schemas

router = APIRouter()

@router.post("/", response_model=List[schemas.ResponseItem])
async def production_plan(payload: schemas.Payload):
    try:
        production_service = ProductionService()
        response = production_service.calculate_production_plan(payload)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    