def build_filter_condition_request(request):
    name_arg = request.args.get("name")
    status_arg = request.args.get("status")
    material_type_arg = request.args.get("material_type")
    price_arg = request.args.get("price")
    body_filter = {}
    if name_arg is not None and len(name_arg) > 0:
        body_filter["name"] = name_arg
    if status_arg is not None and int(status_arg) > 0:
        body_filter["status"] = int(status_arg)
    if material_type_arg is not None and int(material_type_arg) > 0:
        body_filter["material_type"] = int(material_type_arg)

    if price_arg is not None:
        range_price = request.args.get('price').split(",")
        for index in range(len(range_price)):
            try:
                range_price[index] = int(range_price[index])
            except Exception as e:
                print(e)
                return False, "Bad Request: Price Is Invalid"

        if len(range_price) == 2:
            if range_price[0] > range_price[1]:
                body_filter["min_price"] = range_price[1]
                body_filter["max_price"] = range_price[0]
            else:
                body_filter["min_price"] = range_price[0]
                body_filter["max_price"] = range_price[1]
        elif len(range_price) == 1:
            body_filter["min_price"] = range_price[0]
            body_filter["max_price"] = range_price[0]

    return body_filter
