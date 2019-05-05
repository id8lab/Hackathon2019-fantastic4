import paho.mqtt.client as mqttClient
import time
import paho.mqtt.publish as publish
 
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
        client.subscribe("MVPclub")

        client.publish("/frommothership", "Hello")
        client.publish("/frommothership", "World")
 
    else:
 
        print("Connection failed")
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    # publish.single("frommothership", "Hello", hostname="m24.cloudmqtt.com")
    # publish.single("frommothership", "World!", hostname="m24.cloudmqtt.com")
 
Connected = False   #global variable for the state of the connection
 
broker_address= "m24.cloudmqtt.com"  #Broker address
port = 13146                         #Broker port
user = "rdffylha"                    #Connection username
password = "FkRlmEqA63hA"            #Connection password
 
client = mqttClient.Client("MVPclub")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
 
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)
 
client.subscribe("MVPclub")
 
try:
    while True:
        time.sleep(1)
 
except KeyboardInterrupt:
    print ("exiting")
    client.disconnect()
    client.loop_stop()