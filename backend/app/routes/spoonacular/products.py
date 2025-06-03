from fastapi import APIRouter
from dotenv import load_dotenv
import os

# Import environment variables
load_dotenv()

router = APIRouter(
    prefix="/products",
    tags=["Products"],
    responses={
        404: {"description": "Ingredient not found"},
        500: {"description": "Internal Server Error"},
    },
)

API_KEY = os.getenv("SPOONACULAR_API_KEY")
BASE_URL = "https://api.spoonacular.com"

# Endpoint to get information 'bout products for SpoonacularAPI | User search by product (MAYBE)
@router.get("/products")
def get_products_by_title():
   return {"message": "Product search endpoint"}