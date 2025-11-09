class Cat:
    def __init__(self, name, age, weight, activity, neutered):
        self.name = name
        self.age = age
        self.weight = weight
        self.activity = activity
        self.neutered = neutered

    def calculate_calorie(self):
        """base on cat age and act kcal"""
        base = 70 * (self.weight ** 0.75)
        if self.activity == "low":
            factor = 1.2
        elif self.activity == "medium":
            factor = 1.4
        else:
            factor = 1.6

        if self.neutered:
            factor *= 0.9  
        return base * factor

    def info(self):
        return f"{self.name} ({self.weight}kg, {self.activity}, {'neutered' if self.neutered else 'unneutered'})"
