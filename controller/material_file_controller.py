import repository
from provider import MQChannelManager
import services
from flask import jsonify
import model
from http import HTTPStatus


def add_file_material_controller(pg_db, mq_channel, request):
    try:
        material_rp = repository.MaterialRepository(pg_db)
        mq_channel_manager = MQChannelManager(mq_channel)
        material_file_services = services.MaterialFileServices(material_rp, mq_channel_manager)
        result, data = material_file_services.add_file_list_material(request)
        if result is False:
            return jsonify(model.ErrorResponseDto(HTTPStatus.BAD_REQUEST, data).__dict__), HTTPStatus.BAD_REQUEST
        return jsonify(model.SuccessResponseDto(HTTPStatus.OK, "Success").__dict__)
    except Exception as e:
        print(e)
        return jsonify(model.ErrorResponseDto(HTTPStatus.INTERNAL_SERVER_ERROR,
                                              "Internal Error").__dict__), HTTPStatus.INTERNAL_SERVER_ERROR


def download_file_material_controller(pg_db, mq_channel, request):
    try:
        material_rp = repository.MaterialRepository(pg_db)
        mq_channel_manager = MQChannelManager(mq_channel)
        material_file_services = services.MaterialFileServices(material_rp, mq_channel_manager)
        material_file_services.download_file_csv_material(request)
        return jsonify(model.SuccessResponseDto(HTTPStatus.OK, "Success").__dict__)
    except Exception as e:
        print(e)
        return jsonify(
            model.ErrorResponseDto(HTTPStatus.OK, "Internal Error").__dict__), HTTPStatus.INTERNAL_SERVER_ERROR
