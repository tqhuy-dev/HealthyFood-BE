import flask
from flask import request, jsonify


def run_api():
    app = flask.Flask(__name__)

    # app.config["DEBUG"]

    @app.route('/api/v1/food', methods=["GET"])
    def get_all_food():
        result = {
            "code": 200,
            "data": "Success"
        }

        return jsonify(result)

    @app.errorhandler(404)
    def page_not_found(e):
        result = {
            "code": 404,
            "message": "Not Found"
        }
        return jsonify(result)

    app.run(host="0.0.0.0", port=3000)
