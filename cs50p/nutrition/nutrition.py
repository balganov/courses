fruit = input("Item: ").lower().title()
dictionary = {
    "Lemon": 15,
    "Lime":	20,
    "Avocado": 50,
    "Cantaloupe": 50,
    "Honeydew ": 50,
    "Pineapple": 50,
    "Strawberries":	50,
    "Tangerine": 50,
    "Grapefruit": 60,
    "Nectarine": 60,
    "Peach": 60,
    "Plums": 70,
    "Orange": 80,
    "Watermelon": 80,
    "Grapes": 90,
    "Kiwifruit": 90,
    "Pear":	100,
    "Sweet": 100,
    "Banana": 110,
    "Apple": 130,
    "Sweet Cherries": 100

}

if fruit in dictionary:
    print("Calories: ", dictionary.get(fruit))
