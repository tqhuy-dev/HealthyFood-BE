import model


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
