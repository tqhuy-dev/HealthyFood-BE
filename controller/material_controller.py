import services
import model
from http import HTTPStatus
from flask import jsonify
import sys


def add_material_controller(pg_db, request):
    try:
        result, data = services.add_material(pg_db, request)
        if result:
            return jsonify(model.SuccessResponseDto(HTTPStatus.OK, "Success").__dict__)
        else:
            return jsonify(model.ErrorResponseDto(HTTPStatus.BAD_REQUEST, data).__dict__), HTTPStatus.BAD_REQUEST
    except:
        return jsonify(model.ErrorResponseDto(HTTPStatus.INTERNAL_SERVER_ERROR,
                                              "Internal Error").__dict__), HTTPStatus.INTERNAL_SERVER_ERROR
