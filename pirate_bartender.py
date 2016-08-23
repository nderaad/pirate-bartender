import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

responses = {}

def type_of_drink():
    for key in questions:
        inp = input(questions[key].lower())
        if inp == "yes" or inp == "y":
            response = True
        elif inp == "no" or inp == "n":
            response = False
        else:
            print("You need to say Yes or No")
        responses[key] = response
        print(inp)
    print(responses)

type_of_drink()

def make_drink(x):
    drink = []
    for key in ingredients:
        if x[key] == True:
            ingredient = random.choice(ingredients[key])
        elif x[key] == False:
            ingredient = "Nothing Added"
        drink.append(ingredient)
    print(drink)
make_drink(responses)