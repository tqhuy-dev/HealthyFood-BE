import services
import model
from http import HTTPStatus
from flask import jsonify
import repository


def add_food_material_controller(pg_db, request, food_id):
    try:
        food_material_rp = repository.FoodMaterialRepository(pg_db)
        food_material_sv = services.FoodMaterialServices(food_material_rp)
        result, data = food_material_sv.add_food_material_sv(request, food_id)
        if result is False:
            return jsonify(model.ErrorResponseDto(HTTPStatus.BAD_REQUEST, data).__dict__), HTTPStatus.BAD_REQUEST
        return jsonify(model.SuccessResponseDto(HTTPStatus.OK, "Success").__dict__)
    except Exception as e:
        print(e)
        return jsonify(model.ErrorResponseDto(HTTPStatus.INTERNAL_SERVER_ERROR,
                                              "Internal Error").__dict__), HTTPStatus.INTERNAL_SERVER_ERROR
