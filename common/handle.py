import json
import pandas as pd


def convert_dict_list_to_json_str(data):
    result = []
    for item in data:
        result.append(json.dumps(item))

    return result


def convert_nan_to_string(data):
    if pd.isna(data):
        return ""


def convert_nan_to_int(data):
    if pd.isna(data):
        return 0
