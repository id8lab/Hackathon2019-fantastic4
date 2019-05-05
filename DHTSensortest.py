import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#GPIO can have set to BCM or BOARD
#BOARD uses actual Pin Numbers and BCM uses the Broadcom GPIO Numbers
# The Number with GPIO pins are the BCM Numbers and 
# the numbers next to it are the acutal pin numbers

import Adafruit_DHT

#import paho.mqtt.client as mqtt

import time

# Define event callbacks


# 3.3V   - 1      2  - 5V
# GPIO2  - 3      4  - 5V
# GPIO3  - 5      6  - GND
# GPIO4  - 7      8  - GPIO14
# GND    - 9      10 - GPIO15
# GPIO17 - 11     12 - GPIO18
# GPIO27 - 13     14 - GND
# GPIO22 - 15     16 - GPIO23
# 3.3V   - 17     18 - GPIO24
# GPIO10 - 19     20 - GND
# GPIO9  - 21     22 - GPIO25
# GPIO11 - 23     24 - GPIO8
# GND    - 25     26 - GPIO7

#Setting Elecfreaks GPIO Shield Pins with the corresponding GPIO Pins

D2 = 17
D3 = 18
D4 = 27
D5 = 22
D6 = 23
D7 = 24
D8 = 25
D9 = 4
D10 = 8
A3 = 7

GPIO.setup(D8, GPIO.IN)

def on_connect(mosq, obj, rc):
    #print ("on_connect:: Connected with result code "+ str ( rc ) )
    #print("rc: " + str(rc))
    #print("" )
def on_message(mosq, obj, msg):
    #print ("on_message:: this means  I got a message from brokerfor this topic")
    #print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    #print ("")
def on_publish(mosq, obj, mid):
    #print("mid: " + str(mid))
    #print ("")
def on_subscribe(mosq, obj, mid, granted_qos):
    #print("This means broker has acknowledged my subscribe request")
    #print("Subscribed: " + str(mid) + " " + str(granted_qos))
def on_log(mosq, obj, level, string):
    #print(  string)
client = mqtt.Client()
 Assign event callbacks
client.on_message = on_message
client.on_connect = on_connect
client.on_publish = on_publish
client.on_subscribe = on_subscribe


# Uncomment to enable debug messages
client.on_log = on_log
 user name has to be called before connect - my notes.
client.username_pw_set("rdffylha", "FkRlmEqA63hA")
client.connect('m15.cloudmqtt.com', 19119, 60)
client.loop_start()
client.subscribe ("/tempsensor" ,0 )
run = True
while run:
    client.publish ( "/toclientloud", "from python code")
    humidity, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, D8)
    temperature = str(temp)
    humid = str(humidity)
    both = str("Temperature-" + temperature + "-Humidity-" + humid)
    print(both)
    client.publish ( "Data", both)
time.sleep(1)
GPIO.cleanup() # Cleanup the GPIO
