import services
import model
from http import HTTPStatus
from flask import jsonify
import repository
from provider import MQChannelManager


def add_material_controller(pg_db, request):
    try:
        material_rp = repository.MaterialRepository(pg_db)
        material_type_rp = repository.MaterialTypeRepository(pg_db)
        material_sv = services.MaterialServices(material_rp)
        material_sv.set_material_type_rp(material_type_rp)
        result, data = material_sv.add_material_sv(request)
        if result:
            return jsonify(model.SuccessResponseDto(HTTPStatus.OK, "Success").__dict__)
        else:
            return jsonify(model.ErrorResponseDto(HTTPStatus.BAD_REQUEST, data).__dict__), HTTPStatus.BAD_REQUEST
    except Exception as e:
        print(e)
        return jsonify(model.ErrorResponseDto(HTTPStatus.INTERNAL_SERVER_ERROR,
                                              "Internal Error").__dict__), HTTPStatus.INTERNAL_SERVER_ERROR


def get_material_controller(pg_db, request):
    try:
        material_rp = repository.MaterialRepository(pg_db)
        material_sv = services.MaterialServices(material_rp)
        result, data = material_sv.get_material_sv(request)
        if result is False:
            return jsonify(model.ErrorResponseDto(HTTPStatus.BAD_REQUEST, data).__dict__), HTTPStatus.BAD_REQUEST
        return jsonify(model.SuccessResponseDto(HTTPStatus.OK, data).__dict__)
    except Exception as e:
        print(e)
        return jsonify(model.ErrorResponseDto(HTTPStatus.INTERNAL_SERVER_ERROR,
                                              "Internal Error").__dict__), HTTPStatus.INTERNAL_SERVER_ERROR
