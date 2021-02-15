import flask
from flask import request, jsonify
import model
from http import HTTPStatus
import controller


def run_api():
    app = flask.Flask(__name__)

    # app.config["DEBUG"]

    @app.route('/api/v1/food', methods=["GET"])
    def get_all_food():
        return controller.get_all_food_controller(request)

    @app.errorhandler(HTTPStatus.NOT_FOUND)
    def page_not_found(e):
        result = model.ErrorResponseDto(HTTPStatus.NOT_FOUND, "Api Not Found")
        return jsonify(result.__dict__), HTTPStatus.NOT_FOUND

    app.run(host="0.0.0.0", port=3000)
