from fastapi import APIRouter
from dotenv import load_dotenv
import os

# Import environment variables
load_dotenv()

router = APIRouter(
    prefix="/menu",
    tags=["Menu"],
    responses={
        404: {"description": "Ingredient not found"},
        500: {"description": "Internal Server Error"},
    },
)

API_KEY = os.getenv("SPOONACULAR_API_KEY")
BASE_URL = "https://api.spoonacular.com"


# Endpoint to get meal plan templates | User select any recipes and add to list for weekly meal plan
@router.get("/menu")
def get_meal_plan():
    return {"message": "Meal plan endpoint"}

# Endpoint to generate shopping list | User select any recipes and add to list for shopping list

# Endpoint to delete a item of shopping list | User select any recipes (& ingredient) and delete to list for shopping list
