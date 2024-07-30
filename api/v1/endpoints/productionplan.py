from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from api import deps

router = APIRouter()


@router.post("/")
async def get_production_by_plant(
    *,
    db: Session = Depends(deps.get_db),
) -> Any:
    #TODO
    print("prueba")
    return

