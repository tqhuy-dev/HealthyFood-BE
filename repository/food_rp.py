import model
from datetime import date


def get_all_food(pg_db, total):
    sql_query = "SELECT id,name,type_food,price,status,rate,order_total,unit_type " \
                "from public.\"Food\" limit {}".format(total)
    cursor = pg_db.cursor()
    cursor.execute(sql_query)
    record = cursor.fetchall()
    cursor.close()
    list_food = []
    for item in record:
        food = model.Food(item["id"], item["name"], item["type_food"], item["price"], item["status"],
                          item["rate"], item["order_total"],
                          item["unit_type"])
        list_food.append(food)

    return list_food


def add_food(pg_db, food):
    sql_command = "INSERT INTO public.\"Food\"" \
                  "(name, price, status, updated_date, " \
                  "created_date, order_total, rate, unit_type, type_food)" \
                  "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
        food.name, food.price, food.status, date.today(), date.today(), food.order_total, food.rate, food.unit_type,
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
    if "unit_type" in data and data["unit_type"] > 0:
        data_update.append("unit_type = {}".format(data["unit_type"]))
    if "type_food" in data and data["type_food"] > 0:
        data_update.append("type_food = {}".format(data["type_food"]))

    sql_command = "UPDATE public.\"Food\" SET  {} where id = {}".format(",".join(data_update), food_id)
    cursor = pg_db.cursor()
    cursor.execute(sql_command)
    pg_db.commit()
    cursor.close()
