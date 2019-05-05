import paho.mqtt.client as mqtt
import RPi.GPIO as io
#import urllib.parse
import Adafruit_DHT
import time
# Define event callbacks

def GetDistance(Trig, Echo):
    
    io.setmode(io.BCM)
    io.setup(Trig,io.OUT)
    io.setup(Echo,io.IN)

    io.output(Trig,True)
    time.sleep(0.0001)
    io.output(Trig,False)

    while io.input(Echo)== False:
        start=time.time()
    while io.input(Echo)==True:
        stop=time.time()

    distance = (stop-start)*(34200/2)

    return distance


def foo1():
    print("foo1 called")

def on_connect(mosq, obj, rc, temp):
    print ("on_connect:: Connected with result code "+ str ( rc ) )
    client.subscribe("Instructions")
    #print("rc: " + str(rc))
    print("" )
def on_message(mosq, obj, msg):
    data=msg.payload.decode('utf-8')
    if data==foo1:
       foo1()
def on_publish(mosq, obj, mid):
    #print("mid: " + str(mid))
    print ("")
def on_subscribe(mosq, obj, mid, granted_qos):
    print("This means broker has acknowledged my subscribe request")
    print("Subscribed: " + str(mid) + " " + str(granted_qos))
def on_log(mosq, obj, level, string):
    print(  string)
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
    while flag:
        temp, humidity = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
        temp= str(temp)
        distance = GetDistance(24,23)
        humidity= str(humidity)
        client.publish (topic="temp-sensor",payload=temp + ", " + humidity)
        client.publish(topic="distance-sensor", payload=str(distance))
        time.sleep(2)
except KeyboardInterrupt:
    print("CTRL-C Halt Disconnecting")
    client.loop_stop()
    client.disconnect()
#client.subscribe("TempRecieved",0)