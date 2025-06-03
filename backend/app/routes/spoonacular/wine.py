from fastapi import APIRouter
from dotenv import load_dotenv
import os

# Import environment variables
load_dotenv()

router = APIRouter(
    prefix="/wine",
    tags=["Wine"],
    responses={
        404: {"description": "Ingredient not found"},
        500: {"description": "Internal Server Error"},
    },
)

API_KEY = os.getenv("SPOONACULAR_API_KEY")
BASE_URL = "https://api.spoonacular.com"

# Endpoint Dish pairing for wine | User search a recipe that goes well with a wine
@router.get("/wine")
def wine():
    return {"message": "Wine endpoint"}