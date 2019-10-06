import json
import flask
from flask import Flask, request, Response
from flask_cors import CORS

from utils import get_data_from

application = Flask(__name__)
CORS(application)

@application.route('/', methods=["POST"])
def flight_data():
    url = request.json['url']
    data = get_data_from(url)
    return json.dumps(data)

if __name__ == "__main__":
    application.run(host='0.0.0.0')