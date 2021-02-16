import repository
import model
import enum_class
from common import constant


def get_all_food(pg_db, request):
    total = request.args.get('total')
    if total is None:
        total = '100'
    data = repository.get_all_food(pg_db, total)
    food_list = []
    for x in data:
        x.status = enum_class.StatusFoodEnum(x.status).name
        x.type_food = enum_class.FoodTypeEnum(x.type_food).name
        food_list.append(x.__dict__)

        result = (food_list, len(food_list))
    return result


def add_food(pg_db, request):
    data = request.json
    food = model.Food(0, data["name"], data["type_food"], data["price"], data["status"], 0, 5, data["unit_type"])
    repository.add_food(pg_db, food)


def update_status_food(pg_db, request, food_id):
    data = request.json
    if data is None:
        return False, "Body Is Not Valid"
    if data["status"] not in constant.STATUS_FOOD_ARRAY:
        return False, "Status Food Is Not Valid"
    if food_id <= 0:
        return False, "Id Food Is Not Valid"
    repository.update_status_food(pg_db, data["status"], food_id)
    return True, "Success"


def update_info_food(pg_db, request, food_id):
    data = request.json
    if data is None:
        return False, "Body Is Not Valid"
    repository.update_info_food(pg_db, data, food_id)
    return True, "Success"
