# meal.py
import csv
import random

class Meal:
    def __init__(self, calorie):
        self.calorie = calorie
        self.ingredients = self.load_ingredients()

    def load_ingredients(self):
        """from CSV"""
        ingredients = []
        with open("data/ingredients.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                ingredients.append(row)
        return ingredients

    def generate_plan(self):
        """make cat food"""
        protein = random.choice([i for i in self.ingredients if i["Type"] == "Protein"])
        fat = random.choice([i for i in self.ingredients if i["Type"] == "Fat"])
        carb = random.choice([i for i in self.ingredients if i["Type"] == "Carb"])

        self.plan = {
            "protein": protein["Name"],
            "fat": fat["Name"],
            "carb": carb["Name"]
        }
        return self.plan

    def save_to_file(self, cat):
        with open("meal_records.txt", "a", encoding="utf-8") as f:
            f.write(f"{cat.name},{cat.weight},{cat.activity},{self.plan}\n")
        print("already save in meal_records.txt")
