import services
import model
from http import HTTPStatus
from flask import jsonify
import repository
from provider import MQChannelManager


def sync_es_food_controller(pg_db, mq_channel_connect, request):
    try:
        food_rp = repository.FoodRepository(pg_db)
        mq_channel_manager = MQChannelManager(mq_channel_connect)
        sync_food_es_services = services.SyncESFoodServices(food_rp, mq_channel_manager)
        sync_food_es_services.sync_by_list_id(request)
        return jsonify(model.SuccessResponseDto(HTTPStatus.OK,
                                                "Success").__dict__)
    except Exception as e:
        print(e)
        return jsonify(model.ErrorResponseDto(HTTPStatus.INTERNAL_SERVER_ERROR,
                                              "Internal Error").__dict__), HTTPStatus.INTERNAL_SERVER_ERROR
