from pprint import pprint
with open('recipes.txt') as f:
    cook_book = {}
    for line in f:
        dish = line.strip()
        number_of_ingredients = int(f.readline())
        ingredients = []
        for _ in range(number_of_ingredients):
            ingredient_name, quantity, measure = f.readline().strip().split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            })
        f.readline()
        cook_book[dish] = ingredients
    pprint(cook_book, sort_dicts=False)