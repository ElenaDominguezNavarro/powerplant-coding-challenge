import uvicorn
from fastapi import FastAPI, Request
from api.v1.api import api_router
from db.init_db import init_db
from runtimeConstants import SERVER_IP, SERVER_PORT
from constants import URL_PREFIX

init_db()

app = FastAPI(docs_url=URL_PREFIX + "/docs",
              redoc_url=URL_PREFIX + "/redoc", openapi_url=URL_PREFIX + "/openapi.json")

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host=SERVER_IP, port=SERVER_PORT)
