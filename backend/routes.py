from flask import Blueprint, jsonify, request
import openai
from config import OPENAI_API_KEY

routes = Blueprint('routes', __name__)

# Set openai api key
openai.api_key = OPENAI_API_KEY

@routes.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API is running!"})

@routes.route("/generate_recipe", methods=["POST"])
def generate_recipe(): 
    data = request.get_json()
    ingredients = data.get("ingredients", [])

    if not ingredients: 
        return jsonify({"error": "No ingredients provided"}), 400
    
    prompt = f"Create a recipe using the following ingredients: {', '.join(ingredients)}." 

    try:
        response = openai.chat.completions.create(
            model = "gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return jsonify({"recipe": response.choices[0].message.content})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


