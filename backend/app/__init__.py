from fastapi import FastAPI

# Instance of FastAPI
app = FastAPI()

# Importing routes from app.main
from app.main import user

app.include_router(user.router)