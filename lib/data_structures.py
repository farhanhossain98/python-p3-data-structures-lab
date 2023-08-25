spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]
# return [the element we need in the food FOR all all of the food in the list Spicy food]
    

def get_spiciest_foods(spicy_foods):
    return [ food for food in spicy_foods if food['heat_level'] > 5]
# return [all the elements of food for all food in the list spicy food if the heatlevel of food is greater than 5]
    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')
# for all food in spicy food print all elements of food with interpolation. the name, cuisine type, and heat level. The heat level will be listed as the emoji we choose and we will mulitply it by the number of heat level in food. 

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food 
# for all food elements in spicy food. if cuisine in food is equal to the cuisine we search for then return food 

def print_spiciest_foods(spicy_foods):
    spiciest_food = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_food)
# line 41 tells us the spiciest_food is equal to the function get_spiciest_food but the spicy food in the parantheses tells us we only want the spicy food
# line 42 tells us to take the print_spicy_food function and give back to us the spiciest food which we defined. 
# get spiciest food function already made a function that gives us the hottest cuisine and the print spicy food function gives us how we want to label the food.


        # [print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {food["heat_level"]}') for food in spicy_foods if food['heat_level'] > 5]
        # print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    return sum([food["heat_level"] for food in spicy_foods])/ len(spicy_foods)
    # len in pyhton is a function that reutnr the length of the object. in this case the length of the object is 3 and so we take the sum of all the heat levels of food heat level for food in spicy food and divide it by the length of the object 

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
