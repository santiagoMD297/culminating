class Ingredient:
    def __init__(self, name, cals_per_100):
        self.name = name                 
        self.cals_per_100 = float(cals_per_100)  

class CalorieCounter:
    def __init__(self):
        self.foodDB = []   
    def add(self, ing):
        
        self.foodDB.append(ing)

    def find_100(self, food_name):
        
        for ingredient in self.foodDB:
            if ingredient.name == food_name:
                return ingredient.cals_per_100
        return -1.0  

    def cals_for(self, name, grams):
        
        cals100 = self.find_100(name)
        if cals100 == -1.0:
            return 0.0       
        return (cals100 / 100.0) * float(grams)

    def load_foods(self, food_file):
        f = open(food_file, "r")
        for line in f:
            line = line.strip()
            if line == "":      
                continue
            name, cals = line.split()
            self.add(Ingredient(name, cals))

    def count(self, recipe_file):
        
        total = 0.0
        f = open(recipe_file, "r")
        for line in f:
            line = line.strip()
            if line == "":
                continue
            ingredient_name, grams = line.split()
            total += self.cals_for(ingredient_name, grams)
        return total



calorie_counter = CalorieCounter()
calorie_counter.load_foods("table.dat")     
total_calories = calorie_counter.count("pasta.txt")  
print("Total Calories in Recipe:", round(total_calories, 1))