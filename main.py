# main.py

from cat import Cat
from meal import Meal

def main():
    print("Welcome to the Cat Food Configuration System ")
    name = input("Please enter the name of the cat: ")
    age = float(input("Please enter the age of the cat (years): "))
    weight = float(input("Please enter the weight of the cat(kg): "))
    activity = input("Please enter the activity level (low / medium / high): ").lower()
    neutered = input("Is it spayed/neutered? (y/n): ").lower() == "y"

    cat = Cat(name, age, weight, activity, neutered)
    calorie = cat.calculate_calorie()
    print(f"\n{cat.name} The recommended daily calorie intake is approximately {calorie:.2f} kcal")

    meal = Meal(calorie)
    plan = meal.generate_plan()

    print("\nRecommended cat food combinations：")
    for k, v in plan.items():
        print(f"{k}: {v}")
    
    meal.save_to_file(cat)

if __name__ == "__main__":
    main()
