# chatbot/exercise_recommender.py

import random

class ExerciseRecommender:
    def __init__(self):
        self.exercises = {
            "chest": [
                "Bench Press",
                "Incline Dumbbell Press",
                "Push-Ups",
                "Chest Fly",
                "Cable Crossover"
            ],
            "back": [
                "Pull-Ups",
                "Bent Over Row",
                "Lat Pulldown",
                "Deadlift",
                "Seated Row"
            ],
            "legs": [
                "Squats",
                "Leg Press",
                "Lunges",
                "Leg Curl",
                "Calf Raises"
            ],
            "shoulders": [
                "Shoulder Press",
                "Lateral Raises",
                "Front Raises",
                "Shrugs",
                "Upright Row"
            ],
            "arms": [
                "Bicep Curls",
                "Tricep Dips",
                "Skull Crushers",
                "Hammer Curls",
                "Cable Tricep Pushdown"
            ],
            "core": [
                "Plank",
                "Russian Twists",
                "Leg Raises",
                "Bicycle Crunches",
                "Mountain Climbers"
            ]
        }

    def recommend_exercise(self, muscle_group):
        """Recommend a random exercise based on the specified muscle group."""
        if muscle_group in self.exercises:
            return random.choice(self.exercises[muscle_group])
        else:
            return "Sorry, I don't have exercises for that muscle group."

    def get_all_exercises(self):
        """Return a dictionary of all exercises categorized by muscle group."""
        return self.exercises

# Example usage
if __name__ == "__main__":
    recommender = ExerciseRecommender()
    
    print("Welcome to the Exercise Recommender!")
    print("Available muscle groups: chest, back, legs, shoulders, arms, core")
    
    user_input = input("Which muscle group are you interested in? ").lower()
    recommended_exercise = recommender.recommend_exercise(user_input)
    
    print("Recommended Exercise:", recommended_exercise)
    
    # Display all exercises
    print("\nAll Exercises by Muscle Group:")
    all_exercises = recommender.get_all_exercises()
    for group, exercises in all_exercises.items():
        print(f"{group.capitalize()}: {', '.join(exercises)}")