from fastapi import APIRouter, Depends, HTTPException
from typing import List
from api.v1.production_service import ProductionService
from sqlalchemy.orm import Session
from api import deps
import schemas

router = APIRouter()

@router.post("/", response_model=List[schemas.ResponseItem])
async def production_plan(*, payload: schemas.Payload, db: Session = Depends(deps.get_db)):
    try:
        production_service = ProductionService()
        response = await production_service.calculate_production_plan(payload, db)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    