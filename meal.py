import csv
import random
from datetime import datetime

class Meal:
    def __init__(self, calorie):
        self.calorie = calorie
        self.ingredients = self.load_ingredients()

    def load_ingredients(self):
        """Load ingredient data from CSV file"""
        ingredients = []
        with open("foodname.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["Calories_per_100g"] = float(row["Calories_per_100g"])
                ingredients.append(row)
        return ingredients

    def generate_plan(self):
        """Generate a meal plan showing how many grams of each ingredient"""
        protein = random.choice([i for i in self.ingredients if i["Type"] == "Protein"])
        fat = random.choice([i for i in self.ingredients if i["Type"] == "Fat"])
        carb = random.choice([i for i in self.ingredients if i["Type"] == "Carb"])

        # Nutritional ratio assumption: Protein 40%, Fat 30%, Carb 30%
        protein_cal = self.calorie * 0.4
        fat_cal = self.calorie * 0.3
        carb_cal = self.calorie * 0.3

        # Calculate required grams for each ingredient based on calories per 100g
        protein_g = protein_cal / protein["Calories_per_100g"] * 100
        fat_g = fat_cal / fat["Calories_per_100g"] * 100
        carb_g = carb_cal / carb["Calories_per_100g"] * 100

        self.plan = {
            "Protein": f"{protein['Name']} ({protein_g:.1f} g)",
            "Fat": f"{fat['Name']} ({fat_g:.1f} g)",
            "Carbohydrate": f"{carb['Name']} ({carb_g:.1f} g)",
            "Total Calories": f"{self.calorie:.1f} kcal"
        }
        return self.plan

    def save_to_file(self, cat):
        """Save result with timestamp"""
        with open("meal_records.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}, {cat.name}, {cat.weight}kg, {cat.activity}, {self.plan}\n")
        print("\n Meal configuration saved to meal_records.txt")

