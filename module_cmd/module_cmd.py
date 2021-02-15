import flask
from flask import request, jsonify
import model
from http import HTTPStatus
import controller
from gevent.pywsgi import WSGIServer
import configparser


def run_api(cursor):
    app = flask.Flask(__name__)

    # app.config["DEBUG"]

    @app.route('/api/v1/food', methods=["GET"])
    def get_all_food():
        return controller.get_all_food_controller(request, cursor)

    @app.errorhandler(HTTPStatus.NOT_FOUND)
    def page_not_found(e):
        result = model.ErrorResponseDto(HTTPStatus.NOT_FOUND, "Api Not Found")
        return jsonify(result.__dict__), HTTPStatus.NOT_FOUND

    config = configparser.ConfigParser()
    config.read('config.ini')
    if config.get('APP', 'ENVIRONMENT') == 'development':
        app.run(host="127.0.0.1", port=3000)
        if __name__ == "__main__":
            app.run(debug=True)
    else:
        http_server = WSGIServer(('', 3000), app)
        http_server.serve_forever()
