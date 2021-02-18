import json


def convert_dict_list_to_json_str(data):
    result = []
    for item in data:
        result.append(json.dumps(item))

    return result
