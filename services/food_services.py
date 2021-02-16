import repository
import model
import enum_class


def get_all_food(pg_db, request):
    total = request.args.get('total')
    if total is None:
        total = '100'
    data = repository.get_all_food(pg_db, total)
    food_list = []
    for x in data:
        x. status = enum_class.StatusFoodEnum(x.status).name
        food_list.append(x.__dict__)

    result = (food_list, len(food_list))
    return result


def add_food(pg_db, request):
    data = request.json
    food = model.Food(data["name"], data["type_food"], data["price"], data["status"], 0, 5, data["unit_type"])
    repository.add_food(pg_db, food)
