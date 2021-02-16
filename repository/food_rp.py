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
