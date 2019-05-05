from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from sensor import GetValueBoolean, GetDistance, GetTemp, RealTime, RFID, X, UVlight
from displayoled import displaytextoled #displaytextoled("FUCK THIS SHIT \n I am out")
from flask_cors import CORS, cross_origin
import paho.mqtt.client as mqtt
#import urllib.parse
import time

my_app = Flask(__name__, template_folder='.')
cors = CORS(my_app)

sensor_data = {'temp-sensor': [], 'distance-sensor': []}

# @my_app.route('/')
# def hello_world():
#     return 'Hello World!'

@my_app.route('/send-data')
@cross_origin()
def send_data():
    args = request.args
    command = args['command']

    print(args)
    print(command)
    if command == "OpenLight":
        return jsonify({"res": "Operation successful"})
    elif command == "GetDistance":
        print(GetDistance(17,27))
        return jsonify({ "distance": GetDistance(17,27) })
    elif command == "TemperatureHumidity":
        print("TemperatureHumidity")
        print(GetTemp(22))
        return jsonify({ "temperature": GetTemp(22) })
    displaytextoled(command)

    return jsonify(args)

@my_app.route('/')
@cross_origin()
def sample_site():
    message =  "hello, world"
    return render_template('index.html', message=sensor_data)


def on_connect(mosq, obj, rc, temp):
    #print ("on_connect:: Connected with result code "+ str ( rc ) )
    #print("rc: " + str(rc))
    print("" )
def on_message(mosq, obj, msg):
    topic=msg.topic
    data=msg.payload.decode("utf-8")
    # print(topic+" - " + data)
    sensor_data[topic].append(data)
    # print(sensor_data[topic])  

def on_publish(mosq, obj, mid):
    #print("mid: " + str(mid))
    print ("")
def on_subscribe(mosq, obj, mid, granted_qos):
    print("Recieved")
def on_log(mosq, obj, level, string):
    print(  string)

if __name__ == '__main__':

    
    client = mqtt.Client()
    # Assign event callbacks
    client.on_message = on_message
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.on_subscribe = on_subscribe
    # Uncomment to enable debug messages
    client.on_log = on_log
    # user name has to be called before connect - my notes.
    client.username_pw_set("smjlshlt", "6r_8MdvcwVy5")
    client.connect('m24.cloudmqtt.com',13123, 60)
    client.loop_start()
    flag=True
    try:
        # while flag:
        client.subscribe("temp-sensor", 0)
        client.subscribe("distance-sensor",0) 
        time.sleep(2)

        my_app.run(host='0.0.0.0',port=80)
    except KeyboardInterrupt:
        client.loop_stop()
        client.disconnect()



