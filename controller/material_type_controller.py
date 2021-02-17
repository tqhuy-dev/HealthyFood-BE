import services
import model
from http import HTTPStatus
from flask import jsonify
import sys
import repository


def add_material_type_controller(pg_db, request):
    try:
        material_type_rp = repository.MaterialTypeRepository(pg_db)
        material_type_sv = services.MaterialTypeServices(material_type_rp)
        result, data = material_type_sv.add_material_type_sv(request)
        if result is False:
            return jsonify(model.ErrorResponseDto(HTTPStatus.BAD_REQUEST, data).__dict__), HTTPStatus.BAD_REQUEST
        return jsonify(model.SuccessResponseDto(HTTPStatus.OK, "Success").__dict__)
    except:
        return jsonify(model.ErrorResponseDto(HTTPStatus.INTERNAL_SERVER_ERROR,
                                              "Internal Error").__dict__), HTTPStatus.INTERNAL_SERVER_ERROR
