import os
import spacy
import streamlit as st

# Ensure spaCy model is installed
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Sample recipes database
recipes = {
    "pasta": {
        "ingredients": ["pasta", "tomato sauce", "garlic", "olive oil", "parmesan cheese"],
        "instructions": "Boil pasta. Heat olive oil, sauté garlic, add tomato sauce. Mix pasta and sauce, then serve with parmesan cheese."
    },
    "pancakes": {
        "ingredients": ["flour", "milk", "eggs", "baking powder", "sugar", "butter"],
        "instructions": "Mix ingredients, heat a pan, pour batter, and cook until golden brown."
    },
    "salad": {
        "ingredients": ["lettuce", "tomato", "cucumber", "olive oil", "lemon juice", "salt"],
        "instructions": "Chop vegetables, mix in a bowl, add dressing, and serve."
    }
}

def generate_recipe(food_item):
    """Returns the recipe for a given food item."""
    food_item = food_item.lower()
    if food_item in recipes:
        recipe = recipes[food_item]
        return f"### Recipe for {food_item.capitalize()}\n\n**Ingredients:**\n- " + "\n- ".join(recipe['ingredients']) + f"\n\n**Instructions:**\n{recipe['instructions']}"
    else:
        return f"Sorry, I don't have a recipe for {food_item}."

def get_food_from_input(user_input):
    """Extracts food item from user input."""
    doc = nlp(user_input)
    for token in doc:
        if token.text.lower() in recipes:
            return token.text.lower()
    return None

# Streamlit UI
st.title("AI-Powered Recipe Generator 🍽️")

user_input = st.text_input("Enter a food item or ask for a recipe:", "")

if user_input:
    food_item = get_food_from_input(user_input)
    if food_item:
        st.markdown(generate_recipe(food_item))
    else:
        st.warning("I couldn't understand the food item. Please try again.")
