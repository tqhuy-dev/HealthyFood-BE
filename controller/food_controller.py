import services
import model
from http import HTTPStatus
from flask import jsonify
import sys


def get_all_food_controller(request, pg_db):
    try:

        (data_food, total_food) = services.get_all_food(pg_db, request)
        result = {
            "food": data_food,
            "total": total_food
        }
        return jsonify(model.SuccessResponseDto(HTTPStatus.OK, result).__dict__)
    except:
        print(sys.exc_info()[0])
        return jsonify(model.ErrorResponseDto(HTTPStatus.INTERNAL_SERVER_ERROR,
                                              "Internal Error").__dict__), HTTPStatus.INTERNAL_SERVER_ERROR


def add_food_controller(request, pg_db):
    try:
        services.add_food(pg_db, request)
        return jsonify(model.SuccessResponseDto(HTTPStatus.OK, "Add Food Success").__dict__)
    except:
        print(sys.exc_info()[0])
        return jsonify(model.ErrorResponseDto(HTTPStatus.INTERNAL_SERVER_ERROR,
                                              "Internal Error").__dict__), HTTPStatus.INTERNAL_SERVER_ERROR
