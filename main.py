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

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count
            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
            else:
                shop_list[ingredient_name]['quantity'] += quantity
    return shop_list
pprint(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 2,), sort_dicts=False)
    