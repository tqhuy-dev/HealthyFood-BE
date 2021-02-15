import model


def get_all_food(total):
    food_list = []
    for x in range(total):
        food = model.Food("Food Name", "Test", x, 1)
        food_list.append(food.__dict__)

    result = (food_list, len(food_list))
    return result
