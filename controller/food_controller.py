import services
import model
from http import HTTPStatus
from flask import jsonify


def get_all_food_controller(request):
    try:
        total = request.args.get('total')
        (data_food, total_food) = services.get_all_food(int(total))
        result = {
            "food": data_food,
            "total": total_food
        }
        return jsonify(model.SuccessResponseDto(HTTPStatus.OK, result).__dict__)
    except:
        return jsonify(model.ErrorResponseDto(HTTPStatus.INTERNAL_SERVER_ERROR,
                                              "Internal Error").__dict__), HTTPStatus.INTERNAL_SERVER_ERROR
