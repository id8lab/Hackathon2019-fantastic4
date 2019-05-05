import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
    client.subscribe("TempSensor",0)  # Subscribe to the topic “digitest/test1”, receive any messages published on it

def on_subscribe(mosq, obj, mid, granted_qos):
    print("This means broker has acknowledged my subscribe request")
    print("Subscribed: " + str(mid) + " " + str(granted_qos))
def on_message(client, obj, msg):
    data=str(msg.payload)
    print(data)
    #print(msg.topic + " " + str(msg.qos) + " " + data)
    if data is "Hello":
        print("Yippie")


client = mqtt.Client("sensordata")  # Create instance of client with client ID “digi_mqtt_test”
client.on_connect = on_connect  # Define callback function for successful connection
client.on_message = on_message  # Define callback function for receipt of a message
client.on_subscribe = on_subscribe # Define callback function for subscribing to topic
# client.connect("m2m.eclipse.org", 1883, 60)  # Connect to (broker, port, keepalive-time)
client.username_pw_set("smjlshlt", "6r_8MdvcwVy5")
client.connect('m24.cloudmqtt.com', 13123, 60)
client.loop_forever()  #Start networking daemon
client.on_message()

