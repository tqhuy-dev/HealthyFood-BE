import repository
import model


def get_all_food(cursor, total):
    data = repository.get_all_food(cursor, total)
    food_list = []
    for x in data:
        food_list.append(x.__dict__)

    result = (food_list, len(food_list))
    return result


def add_food(cursor, request):
    data = request.json
    food = model.Food(data["name"], data["type_food"], data["price"], data["status"], 0, 5, data["unit_type"])
    repository.add_food(cursor, food)
