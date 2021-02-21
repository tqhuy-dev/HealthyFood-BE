import repository
from provider import MQChannelManager
import services
from flask import jsonify
import model
from http import HTTPStatus


def download_file_food_controller(pg_db, mq_channel_connect, request):
    try:
        food_rp = repository.FoodRepository(pg_db)
        mq_channel_manager = MQChannelManager(mq_channel_connect)
        food_file_sv = services.FoodFileServices(food_rp, mq_channel_manager)
        food_file_sv.download_file_food(request)
        return jsonify(model.SuccessResponseDto(HTTPStatus.OK, "Success").__dict__)
    except Exception as e:
        print(e)
        return jsonify(
            model.ErrorResponseDto(HTTPStatus.INTERNAL_SERVER_ERROR,
                                   "Internal Error").__dict__), HTTPStatus.INTERNAL_SERVER_ERROR


def add_file_food_controller(pg_db, mq_channel_connect, request):
    try:
        food_rp = repository.FoodRepository(pg_db)
        mq_channel_manager = MQChannelManager(mq_channel_connect)
        food_file_sv = services.FoodFileServices(food_rp, mq_channel_manager)
        result, data = food_file_sv.add_food_by_file(request)
        if result is False:
            return jsonify(
                model.ErrorResponseDto(HTTPStatus.BAD_REQUEST, data).__dict__), HTTPStatus.BAD_REQUEST
        return jsonify(model.SuccessResponseDto(HTTPStatus.OK, "Success").__dict__)
    except Exception as e:
        print(e)
        return jsonify(
            model.ErrorResponseDto(HTTPStatus.INTERNAL_SERVER_ERROR,
                                   "Internal Error").__dict__), HTTPStatus.INTERNAL_SERVER_ERROR
