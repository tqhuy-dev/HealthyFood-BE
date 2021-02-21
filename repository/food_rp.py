import model
from datetime import date


class FoodRepository(object):
    def __init__(self, pg_db):
        self.pg_db = pg_db

    def get_all_food(self, filter_body):
        sql_condition_arr = ["1=1"]

        if "name" in filter_body:
            sql_condition_arr.append("name like '%{}%'".format(filter_body["name"]))
        if "min_price" in filter_body and "max_price" in filter_body:
            sql_condition_arr.append(
                "price >= {} and price <= {}".format(filter_body["min_price"], filter_body["max_price"]))
        if "food_type" in filter_body:
            sql_condition_arr.append("type_food = {}".format(filter_body["food_type"]))
        if "from_id" in filter_body and "to_id" in filter_body:
            sql_condition_arr.append(
                "id >= {} and id <= {}".format(filter_body["from_id"], filter_body["to_id"]))

        sql_condition = " and ".join(sql_condition_arr)
        sql_query = "SELECT id,name,type_food,price,status,rate,order_total,unit,type_food,image " \
                    "from public.\"Food\" where {} limit {}".format(sql_condition, filter_body["total"])
        cursor = self.pg_db.cursor()
        cursor.execute(sql_query)
        record = cursor.fetchall()
        cursor.close()
        list_food = []
        for item in record:
            food = model.Food(item["id"], item["name"], item["type_food"], int(item["price"]), item["status"],
                              item["order_total"], item["rate"],
                              item["unit"])
            food.set_image(item["image"])
            list_food.append(food)

        return list_food

    def add_list_food(self, list_food):
        sql_item_arr = []
        for food in list_food:
            sql_item_arr.append("('{}', {}, {}, '{}', '{}', {}, {}, '{}', {}, '{}') ".
                                format(food.name, food.price, food.status, date.today(), date.today(), food.order_total,
                                       food.rate, food.unit,
                                       food.type_food, food.image))
        sql_command = "INSERT INTO public.\"Food\"" \
                      "(name, price, status, updated_date, " \
                      "created_date, order_total, rate, unit, type_food,image)" \
                      "VALUES {}".format(",".join(sql_item_arr))

        cursor = self.pg_db.cursor()
        cursor.execute(sql_command)
        self.pg_db.commit()
        cursor.close()


def get_all_food(pg_db, filter_body):
    sql_condition_arr = ["1=1"]

    if "name" in filter_body:
        sql_condition_arr.append("name like '%{}%'".format(filter_body["name"]))
    if "min_price" in filter_body and "max_price" in filter_body:
        sql_condition_arr.append(
            "price >= {} and price <= {}".format(filter_body["min_price"], filter_body["max_price"]))
    if "food_type" in filter_body:
        sql_condition_arr.append("type_food = {}".format(filter_body["food_type"]))
    if "from_id" in filter_body and "to_id" in filter_body:
        sql_condition_arr.append(
            "id >= {} and id <= {}".format(filter_body["from_id"], filter_body["to_id"]))

    sql_condition = " and ".join(sql_condition_arr)
    sql_query = "SELECT id,name,type_food,price,status,rate,order_total,unit,type_food " \
                "from public.\"Food\" where {} limit {}".format(sql_condition, filter_body["total"])
    cursor = pg_db.cursor()
    cursor.execute(sql_query)
    record = cursor.fetchall()
    cursor.close()
    list_food = []
    for item in record:
        food = model.Food(item["id"], item["name"], item["type_food"], int(item["price"]), item["status"],
                          item["rate"], item["order_total"],
                          item["unit"])
        list_food.append(food)

    return list_food


def add_food(pg_db, food):
    sql_command = "INSERT INTO public.\"Food\"" \
                  "(name, price, status, updated_date, " \
                  "created_date, order_total, rate, unit, type_food)" \
                  "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')". \
        format(food.name, food.price, food.status, date.today(), date.today(), food.order_total, food.rate, food.unit,
               food.type_food)

    cursor = pg_db.cursor()
    cursor.execute(sql_command)
    pg_db.commit()
    cursor.close()


def update_status_food(pg_db, status, food_id):
    sql_command = "UPDATE public.\"Food\" SET status={} WHERE Id = {}".format(status, food_id)
    cursor = pg_db.cursor()
    cursor.execute(sql_command)
    pg_db.commit()
    cursor.close()


def update_info_food(pg_db, data, food_id):
    data_update = []
    if "name" in data and len(data["name"]) > 0:
        data_update.append("name = '{}'".format(data["name"]))
    if "price" in data and data["price"] > 0:
        data_update.append("price = {}".format(data["price"]))
    if "unit" in data and len(data["unit"]) > 0:
        data_update.append("unit = '{}'".format(data["unit"]))
    if "type_food" in data and data["type_food"] > 0:
        data_update.append("type_food = {}".format(data["type_food"]))

    sql_command = "UPDATE public.\"Food\" SET  {} where id = {}".format(",".join(data_update), food_id)
    cursor = pg_db.cursor()
    cursor.execute(sql_command)
    pg_db.commit()
    cursor.close()
