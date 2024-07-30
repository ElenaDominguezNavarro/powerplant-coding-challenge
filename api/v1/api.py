from fastapi import APIRouter
from api.v1.endpoints import productionplan
from constants import URL_PREFIX

api_router = APIRouter(prefix=URL_PREFIX)
api_router.include_router(productionplan.router, prefix="/productionplan", tags=["Productionplan"])
