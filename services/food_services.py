import repository


def get_all_food(cursor, total):
    data = repository.get_all_food(cursor, total)
    food_list = []
    for x in data:
        food_list.append(x.__dict__)

    result = (food_list, len(food_list))
    return result
