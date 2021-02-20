import repository
import model
import enum_class
from common import constant


def get_all_food(pg_db, request):
    total = request.args.get('total')
    if total is None:
        total = 100
    total = int(total)
    if total > 100 or total < 0:
        total = 100

    filter_body = {"total": total}
    if request.args.get('price') is not None:
        range_price = request.args.get('price').split(",")
        for index in range(len(range_price)):
            try:
                range_price[index] = int(range_price[index])
            except Exception as e:
                print(e)
                return False, "Bad Request: Price Is Invalid"

        if len(range_price) == 2:
            if range_price[0] > range_price[1]:
                filter_body["min_price"] = range_price[1]
                filter_body["max_price"] = range_price[0]
            else:
                filter_body["min_price"] = range_price[0]
                filter_body["max_price"] = range_price[1]
        elif len(range_price) == 1:
            filter_body["min_price"] = range_price[0]
            filter_body["max_price"] = range_price[0]

    if request.args.get('food_type') is not None:
        try:
            filter_body["food_type"] = int(request.args.get('food_type'))
        except Exception as e:
            print(e)
            return False, "Bad Request: food_type is invalid"

    if request.args.get('name') is not None:
        filter_body["name"] = request.args.get('name')

    data = repository.get_all_food(pg_db, filter_body)
    food_list = []
    for x in data:
        x.status = enum_class.StatusFoodEnum(x.status).name
        x.type_food = enum_class.FoodTypeEnum(x.type_food).name
        food_list.append(x.__dict__)

    result = {
        "Food": food_list,
        "Total": len(food_list)
    }
    return True, result


def add_food(pg_db, request):
    data = request.json
    food = model.Food(0, data["name"], data["type_food"], data["price"], data["status"], 0, 5, data["unit"])
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


def food_filter():
    food_type_array = []
    for item in constant.FOOD_TYPE_ARRAY:
        enum_food_type = enum_class.FoodTypeEnum(item)
        food_type_item = model.FoodTypeModel(enum_food_type.value, enum_food_type.name)
        food_type_array.append(food_type_item.get_dict())

    result = {
        "food_type": food_type_array
    }

    return result
