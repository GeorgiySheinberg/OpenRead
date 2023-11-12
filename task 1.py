from pprint import pprint


def create_cook_book(file_name):
    with open(file_name, 'r', encoding='utf-8') as recipes:

        cook_book = {}
        for line in recipes:
            some_list = line.strip().split(' | ')
            if len(some_list[0]) > 1 and len(some_list) == 1:
                key = some_list[0]
                cook_book.setdefault(key, [])
            elif len(some_list) > 1:
                cook_book[key].append({'ingredient_name': some_list[0], 'quantity': some_list[1],
                                       'measure': some_list[2]})
        pprint(cook_book)


create_cook_book("recipes.txt")
