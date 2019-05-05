from flask import Flask
from flask import request
from flask import jsonify
from sensor import getValueBoolean GetDistance GetTemp RealTime RFID X UVLight
from flask_cors import CORS, cross_origin

my_app = Flask(__name__)
cors = CORS(my_app)

@my_app.route('/')
def hello_world():
    return 'Hello World!'

@my_app.route('/send-data')
@cross_origin()
def send_data():
    args = request.args
    command = args['command']

    print(args)
    print(command)
    if command == "openLight":
        return jsonify({"res": "Operation successful"})
    elif command == "GetDistance":
        return GetDistance(17,27)
    elif command == "TemperatureHumidity":
        return GetTemp(22)
    

    return jsonify(args)

if __name__ == '__main__':
    my_app.run(host='0.0.0.0',port=80)

