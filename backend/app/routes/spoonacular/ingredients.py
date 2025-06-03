from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.models.db_recipes import Ingredient as IngredientModel
from app.schemas.recipe import Ingredient as IngredientSchema
from app.schemas.recipe import IngredientSubstitute as IngredientSubstituteSchema
from app.schemas.recipe import IngredientInfo as IngredientInfoSchema
from app.db.database import get_db
from dotenv import load_dotenv
import os, requests

# Import environment variables
load_dotenv()

router = APIRouter(
    prefix="/ingredient",
    tags=["Ingredients"],
    responses={
        404: {"description": "Ingredient not found"},
        500: {"description": "Internal Server Error"},
    },
)

API_KEY = os.getenv("SPOONACULAR_API_KEY")
BASE_URL = "https://api.spoonacular.com"


#     ------------------      Endpoint search ingredients for SpoonacularAPI | User filter by ingredients      ------------------      

@router.get("/search", response_model=list[IngredientSchema])
def search_ingredients(
    query: str = Query(..., description="Search query for ingredients"),
    number: int = Query(10, ge=10, le=50, description="Number of results to return"),
    db: Session = Depends(get_db)
):

    # Use API if not found in the database
    response = requests.get(
        f"{BASE_URL}/food/ingredients/search",
        params={
            "query": query,
            "number": number,
            "apiKey": API_KEY
        },
    )

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to fetch ingredients from API")

    results = response.json().get("results", [])

    if not results:
        raise HTTPException(status_code=404, detail="Ingredients not found")

    # Save in the database
    saved_ingredients = []
    for ingredient in results:
        existing_ingredient = db.query(IngredientModel).filter_by(spoonacular_id=ingredient["id"]).first()
        if existing_ingredient:
            saved_ingredients.append(existing_ingredient)
            continue

        new_ingredient = IngredientModel(
            spoonacular_id=ingredient["id"],
            name=ingredient["name"],
            image=ingredient["image"],
        )
        db.add(new_ingredient)
        saved_ingredients.append(new_ingredient)

    db.commit()

    # Avoid duplicates in the response
    unique_ingredients = {ingredient.spoonacular_id: ingredient for ingredient in saved_ingredients}

    return list(unique_ingredients.values())

#     ------------------      Endpoint get parse ingredient information | resume ingredient information (calories, carbs, fat, protein, etc.)     ------------------ 

@router.get("/info/{ingredient_id}", response_model=IngredientInfoSchema)
def get_ingredient_info(ingredient_id: int):
    """
    Get nutritional information for a specific ingredient by ID.
    """
    response = requests.get(
        f"{BASE_URL}/food/ingredients/{ingredient_id}/information",
        params={"apiKey": API_KEY, "amount": 100, "unit": "g"},
    )

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to fetch ingredient info from API")

    data = response.json()

    return {
        "id": data.get("id"),
        "name": data.get("name"),
        "image": data.get("image"),
        "calories": data.get("nutrition", {}).get("nutrients", [])[0].get("amount"),
        "carbs": next((n.get("amount") for n in data.get("nutrition", {}).get("nutrients", []) if n.get("name") == "Carbohydrates"), None),
        "fat": next((n.get("amount") for n in data.get("nutrition", {}).get("nutrients", []) if n.get("name") == "Fat"), None),
        "protein": next((n.get("amount") for n in data.get("nutrition", {}).get("nutrients", []) if n.get("name") == "Protein"), None),
    }

#     ------------------      Endpoint to get substitutes for ingredients | get substitutes for a list of ingredients (e.g. gluten-free, dairy-free, etc.)      

@router.get("/substitutes/{ingredient_name}", response_model=IngredientSubstituteSchema)
def get_ingredient_substitutes(ingredient_name: str):
    response = requests.get(
        f"{BASE_URL}/food/ingredients/substitutes",
        params={"ingredientName": ingredient_name, "apiKey": API_KEY},
    )

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to fetch substitutes from API")

    data = response.json()

    if not data.get("substitutes"):
        raise HTTPException(status_code=404, detail="No substitutes found for this ingredient")

    return {
        "ingredient": ingredient_name,
        "substitutes": data.get("substitutes", []),
        "message": data.get("message", "")
    }



#     ------------------      Endpoint convert amounts | convert amounts (grams, ounces, cups, etc.)     ------------------      

#    Endpoint Compute glycemic index & load | compute glycemic index (low, medium, high) and total glycemic load for a list of ingredients (total & per serving)

 