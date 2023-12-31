from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import router.login.login_controller as login
import router.gened.gened_controller as gened

app = FastAPI(
    title="Gened API",
    description="API for Gened",
    version="1.0.0",
)

api_preix = "/api/v1"

app.include_router(login.router, prefix=api_preix)
app.include_router(gened.router, prefix=api_preix)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
