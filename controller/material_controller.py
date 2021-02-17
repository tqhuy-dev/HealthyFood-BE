import services
import model
from http import HTTPStatus
from flask import jsonify
import sys
import repository


def add_material_controller(pg_db, request):
    try:
        material_rp = repository.MaterialRepository(pg_db)
        material_type_rp = repository.MaterialTypeRepository(pg_db)
        material_sv = services.MaterialServices(material_rp)
        material_sv.set_material_type_rp(material_type_rp)
        result, data = material_sv.add_material(request)
        if result:
            return jsonify(model.SuccessResponseDto(HTTPStatus.OK, "Success").__dict__)
        else:
            return jsonify(model.ErrorResponseDto(HTTPStatus.BAD_REQUEST, data).__dict__), HTTPStatus.BAD_REQUEST
    except:
        return jsonify(model.ErrorResponseDto(HTTPStatus.INTERNAL_SERVER_ERROR,
                                              "Internal Error").__dict__), HTTPStatus.INTERNAL_SERVER_ERROR
