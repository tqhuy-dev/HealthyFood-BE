def build_food_filter_condition_request(request):
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

    return filter_body
