from cat import Cat
from meal import Meal

def main():
    print(" Welcome to the Cat Food Configuration System ")

    name = input("Please enter the name of the cat: ").strip() or "Unnamed"

    while True:
        try:
            age = float(input("Please enter the age of the cat (years): "))
            break
        except ValueError:
            print("Please enter a valid number for age!")

    while True:
        try:
            weight = float(input("Please enter the weight of the cat (kg): "))
            break
        except ValueError:
            print("Please enter a valid number for weight!")

    while True:
        activity = input("Please enter the activity level (low / medium / high): ").lower().strip()
        if activity in ["low", "medium", "high"]:
            break
        else:
            print("Please enter only: low, medium, or high.")

    while True:
        neutered = input("Has the cat been neutered? (y/n): ").lower().strip()
        if neutered in ["y", "n"]:
            neutered = (neutered == "y")
            break
        else:
            print("Please enter y or n.")

    cat = Cat(name, age, weight, activity, neutered)
    calorie = cat.calculate_calorie()
    print(f"\n{cat.name} needs about {calorie:.2f} kcal per day.")

    meal = Meal(calorie)
    plan = meal.generate_plan()

    print("Recommended cat meal plan:")
    for k, v in plan.items():
        print(f"{k}: {v}")

    meal.save_to_file(cat)

if __name__ == "__main__":
    main()
