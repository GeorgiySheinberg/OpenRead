from pprint import pprint


def get_shop_list_by_dishes(dishes, person_count):
    with open('recipes.txt', 'r', encoding='utf-8') as recipes:
        cook_book = {}
        for line in recipes:
            some_list = line.strip().split(' | ')
            if len(some_list[0]) > 1 and len(some_list) == 1:
                key = some_list[0]
                cook_book.setdefault(key, [])
            elif len(some_list) > 1:
                cook_book[key].append(
                    {'ingredient_name': some_list[0], 'quantity': some_list[1], 'measure': some_list[2]})
    result = {}
    for dish in dishes:
        for ingredients in cook_book[dish]:
            if result.get(ingredients['ingredient_name']) is None:
                result.setdefault(ingredients['ingredient_name'], {'measure': ingredients['measure'],
                                                                   'quantity': int(
                                                                       ingredients['quantity']) * person_count})
            else:
                result[ingredients['ingredient_name']]['quantity'] += int(ingredients['quantity'])
    pprint(result)


get_shop_list_by_dishes(['Фахитос', 'Омлет', 'Запеченный картофель', 'Утка по-пекински'], 2)
