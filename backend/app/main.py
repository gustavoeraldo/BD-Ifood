from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.api_v1.api import api_router
from core import config

'''
run the project using : uvicorn app.main:app --reload
http://localhost:8000/redoc - redoc 
http://localhost:8000/docs- documentation JSON
'''

app = FastAPI()

origins = [
  "http://localhost:8080",
  "http://localhost"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

app.include_router(api_router, prefix=config.API_V1_STR)
