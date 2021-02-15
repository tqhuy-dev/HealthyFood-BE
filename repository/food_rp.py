import model
from datetime import date


def get_all_food(cursor, total):
    sql_query = "SELECT * from public.\"Food\" limit {}".format(total)
    cursor.execute(sql_query)
    record = cursor.fetchall()
    list_food = []
    for item in record:
        food = model.Food(item["name"], item["type_food"], item["price"], item["status"],
                          item["rate"], item["order_total"],
                          item["unit_type"])
        list_food.append(food)

    return list_food


def add_food(cursor, food):
    sql_command = "INSERT INTO public.\"Food\"" \
                  "(name, price, status, updated_date, " \
                  "created_date, order_total, rate, unit_type, type_food)" \
                  "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
        food.name, food.price, food.status, date.today(), date.today(), food.order_total, food.rate, food.unit_type,
        food.type_food)

    cursor.execute(sql_command)
