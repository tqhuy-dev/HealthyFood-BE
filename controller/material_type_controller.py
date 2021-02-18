import services
import model
from http import HTTPStatus
from flask import jsonify
import provider
import repository


def add_material_type_controller(pg_db, redis_connect, request):
    try:
        material_type_rp = repository.MaterialTypeRepository(pg_db)
        material_type_sv = services.MaterialTypeServices(material_type_rp)
        redis_manager = provider.RedisManager(redis_connect)
        material_type_sv.set_redis_manager(redis_manager)
        result, data = material_type_sv.add_material_type_sv(request)
        if result is False:
            return jsonify(model.ErrorResponseDto(HTTPStatus.BAD_REQUEST, data).__dict__), HTTPStatus.BAD_REQUEST
        return jsonify(model.SuccessResponseDto(HTTPStatus.OK, "Success").__dict__)
    except:
        return jsonify(model.ErrorResponseDto(HTTPStatus.INTERNAL_SERVER_ERROR,
                                              "Internal Error").__dict__), HTTPStatus.INTERNAL_SERVER_ERROR


def get_material_type_controller(pg_db, redis_connect, request):
    try:
        material_type_rp = repository.MaterialTypeRepository(pg_db)
        material_type_sv = services.MaterialTypeServices(material_type_rp)
        redis_manager = provider.RedisManager(redis_connect)
        material_type_sv.set_redis_manager(redis_manager)
        result, data = material_type_sv.get_material_type_sv(request)
        if result is True:
            return jsonify(model.SuccessResponseDto(HTTPStatus.OK, data).__dict__)
        else:
            return jsonify(model.ErrorResponseDto(HTTPStatus.BAD_REQUEST, data).__dict__), HTTPStatus.BAD_REQUEST
    except:
        return jsonify(model.ErrorResponseDto(HTTPStatus.INTERNAL_SERVER_ERROR,
                                              "Internal Error").__dict__), HTTPStatus.INTERNAL_SERVER_ERROR
