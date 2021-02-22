import services
import model
from http import HTTPStatus
from flask import jsonify
import repository
import provider


def get_all_food_controller(pg_db, es, request):
    try:
        food_rp = repository.FoodRepository(pg_db)
        elasticsearch_manager = provider.ElasticsearchManager(es)
        food_sv = services.FoodServices(food_rp, elasticsearch_manager)
        result = food_sv.search_food_elasticsearch(request)
        return jsonify(model.SuccessResponseDto(HTTPStatus.OK, result).__dict__)
    except Exception as e:
        print(e)
        return jsonify(model.ErrorResponseDto(HTTPStatus.INTERNAL_SERVER_ERROR,
                                              "Internal Error").__dict__), HTTPStatus.INTERNAL_SERVER_ERROR


def add_food_controller(request, pg_db):
    try:
        services.add_food(pg_db, request)
        return jsonify(model.SuccessResponseDto(HTTPStatus.OK, "Add Food Success").__dict__)
    except Exception as e:
        print(e)
        return jsonify(model.ErrorResponseDto(HTTPStatus.INTERNAL_SERVER_ERROR,
                                              "Internal Error").__dict__), HTTPStatus.INTERNAL_SERVER_ERROR


def update_status_food_controller(request, pg_db, food_id):
    try:
        result, message = services.update_status_food(pg_db, request, int(food_id))
        if result:
            return jsonify(model.SuccessResponseDto(HTTPStatus.OK, "Update Status Food Success").__dict__)
        else:
            return jsonify(model.ErrorResponseDto(HTTPStatus.BAD_REQUEST, message).__dict__), HTTPStatus.BAD_REQUEST
    except Exception as e:
        print(e)
        return jsonify(model.ErrorResponseDto(HTTPStatus.INTERNAL_SERVER_ERROR,
                                              "Internal Error").__dict__), HTTPStatus.INTERNAL_SERVER_ERROR


def update_info_food_controller(request, pg_db, food_id):
    try:
        result, message = services.update_info_food(pg_db, request, food_id)
        if result:
            return jsonify(model.SuccessResponseDto(HTTPStatus.OK, "Update Food Success").__dict__)
        else:
            return jsonify(model.ErrorResponseDto(HTTPStatus.BAD_REQUEST, message).__dict__), HTTPStatus.BAD_REQUEST
    except Exception as e:
        print(e)
        return jsonify(model.ErrorResponseDto(HTTPStatus.INTERNAL_SERVER_ERROR,
                                              "Internal Error").__dict__), HTTPStatus.INTERNAL_SERVER_ERROR


def get_food_filter_controller():
    try:
        result = services.food_filter()
        return jsonify(model.SuccessResponseDto(HTTPStatus.OK, result).__dict__)
    except Exception as e:
        print(e)
        return jsonify(model.ErrorResponseDto(HTTPStatus.INTERNAL_SERVER_ERROR,
                                              "Internal Error").__dict__), HTTPStatus.INTERNAL_SERVER_ERROR
