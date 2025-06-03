from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

# Model for the Recipe table in the database
# This model defines the structure of the Recipe table and its columns.
class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    image = Column(String, index=True)
    spoonacular_id = Column(Integer, unique=True, index=True)
    instructions = Column(String, index=True)
    cached = Column(Boolean, default=True)
    meal_type = Column(String, nullable=True) 
    diet = Column(String, nullable=True)      
    prep_time = Column(Integer, nullable=True)
    
    #Relationships with ingredients
    ingredients = relationship("RecipeIngredient", back_populates="recipe", cascade="all, delete-orphan")

    #Relationships with similar recipes
    similar_recipes = relationship("SimilarRecipe", back_populates="recipe", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Recipe(id={self.id}, title={self.title}, image={self.image})>"
    
class SimilarRecipe(Base):
    __tablename__ = "similar_recipes"

    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"), index=True)
    similar_recipe_id = Column(Integer, index=True)
    title = Column(String, index=True)
    image = Column(String, index=True)
    
    recipe = relationship("Recipe", back_populates="similar_recipes")


    
class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredients"

    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    ingredients = Column(String)
    quantity = Column(String, nullable = True)
    unit = Column(String, nullable = True)

    recipe = relationship("Recipe", back_populates="ingredients")
    
    
class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True)
    spoonacular_id = Column(Integer, unique=True, index=True)
    name = Column(String, index=True)
    image = Column(String, index=True)
