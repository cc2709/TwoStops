from fastapi import FastAPI
from twostops.api.utils import router as utils_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["chrome-extension://ckhhhihegjdkfjoolgcpoalijiaocacl"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(utils_router)
