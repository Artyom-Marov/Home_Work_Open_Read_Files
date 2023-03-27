# Task_1
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

# Task_2    
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
    
# Task_3
file_names = ['1.txt', '2.txt', '3.txt']
files_data = []

for file_name in file_names:
    with open(file_name) as f:
        lines = f.readlines()
        num_lines = len(lines)
    files_data.append({'name': file_name, 'num_lines': num_lines, 'content': lines})

files_data.sort(key=lambda x: x['num_lines'])

with open('result.txt', 'w') as f:
    for file_data in files_data:
        f.write('\n' + file_data['name'] + '\n')
        f.write(str(file_data['num_lines']) + '\n')
        for line in file_data['content']:
            f.write(line)

    