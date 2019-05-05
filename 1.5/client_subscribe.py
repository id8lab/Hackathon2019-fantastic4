import paho.mqtt.client as mqtt
#import urllib.parse
import time
# Define event callbacks

def foo1():
    print("foo1 called")
    
def on_connect(mosq, obj, rc, temp):
    #print ("on_connect:: Connected with result code "+ str ( rc ) )
    #print("rc: " + str(rc))
    print("" )
def on_message(mosq, obj, msg):
    topic=msg.topic
    data=msg.payload.decode("utf-8")
    print(topic+" - " + data)
    #if(data == "foo1"):
    #   foo1()
def on_publish(mosq, obj, mid):
    #print("mid: " + str(mid))
    print ("")
def on_subscribe(mosq, obj, mid, granted_qos):
    print("Recieved")
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
        client.subscribe("temp-sensor", 0)
        client.subscribe("distance-sensor",0) 
        time.sleep(2)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
#client.subscribe("TempRecieved",0)