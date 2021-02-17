import flask
from flask import request, jsonify
import model
from http import HTTPStatus
import controller
from gevent.pywsgi import WSGIServer
import configparser


def run_api(pg_db):
    app = flask.Flask(__name__)

    @app.route('/api/v1/food', methods=["GET"])
    def get_all_food():
        return controller.get_all_food_controller(request, pg_db)

    @app.route('/api/v1/food', methods=["POST"])
    def add_food():
        return controller.add_food_controller(request, pg_db)

    @app.route('/api/v1/food/status/<food_id>', methods=["PUT"])
    def update_status_food(food_id):
        return controller.update_status_food_controller(request, pg_db, food_id)

    @app.route('/api/v1/food/<food_id>', methods=["PUT"])
    def update_info_food(food_id):
        return controller.update_info_food_controller(request, pg_db, food_id)

    @app.route('/api/v1/food/filter', methods=["GET"])
    def food_filter():
        return controller.get_food_filter_controller()

    @app.route('/api/v1/material', methods=["POST"])
    def add_material():
        return controller.add_material_controller(pg_db, request)

    @app.route('/api/v1/material_type', methods=["POST"])
    def add_material_type():
        return controller.add_material_type_controller(pg_db, request)

    @app.route('/api/v1/material_type', methods=["GET"])
    def get_material_type():
        return controller.get_material_type_controller(pg_db, request)

    @app.errorhandler(HTTPStatus.NOT_FOUND)
    def page_not_found(e):
        result = model.ErrorResponseDto(HTTPStatus.NOT_FOUND, "Api Not Found")
        return jsonify(result.__dict__), HTTPStatus.NOT_FOUND

    config = configparser.ConfigParser()
    config.read('config.ini')
    if config.get('APP', 'ENVIRONMENT') == 'development':
        app.run(host="127.0.0.1", port=3000, debug=False)
    else:
        http_server = WSGIServer(('', 3000), app)
        http_server.serve_forever()
