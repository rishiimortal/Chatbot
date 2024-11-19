# chatbot/nutrition_recommender.py

class NutritionRecommender:
    def __init__(self):
        self.food_sources = {
            "proteins": [
                "Chicken Breast",
                "Turkey",
                "Fish (Salmon, Tuna)",
                "Eggs",
                "Greek Yogurt",
                "Tofu",
                "Lentils",
                "Chickpeas",
                "Quinoa",
                "Nuts (Almonds, Walnuts)"
            ],
            "fats": [
                "Avocado",
                "Olive Oil",
                "Coconut Oil",
                "Butter",
                "Cheese",
                "Fatty Fish (Mackerel, Sardines)",
                "Nuts and Seeds (Chia, Flaxseed)",
                "Dark Chocolate",
                "Nut Butters (Peanut, Almond)",
                "Full-Fat Dairy"
            ],
            "carbohydrates": [
                "Brown Rice",
                "Quinoa",
                "Oats",
                "Whole Wheat Bread",
                "Sweet Potatoes",
                "Fruits (Bananas, Apples)",
                "Vegetables (Broccoli, Spinach)",
                "Legumes (Beans, Lentils)",
                "Pasta (Whole Grain)",
                "Cereals (Whole Grain)"
            ]
        }

    def get_food_sources(self, macro):
        """Return a list of food sources for the specified macronutrient."""
        if macro in self.food_sources:
            return self.food_sources[macro]
        else:
            return "Sorry, I don't have food sources for that macronutrient."

    def get_all_food_sources(self):
        """Return a dictionary of all food sources categorized by macronutrient."""
        return self.food_sources

# Example usage
if __name__ == "__main__":
    recommender = NutritionRecommender()
    
    print("Welcome to the Nutrition Recommender!")
    print("Available macronutrients: proteins, fats, carbohydrates")
    
    user_input = input("Which macronutrient are you interested in? ").lower()
    food_sources = recommender.get_food_sources(user_input)
    
    print("Food Sources:", food_sources)
    
    # Display all food sources
    print("\nAll Food Sources by Macronutrient:")
    all_food_sources = recommender.get_all_food_sources()
    for macro, foods in all_food_sources.items():
        print(f"{macro.capitalize()}: {', '.join(foods)}")