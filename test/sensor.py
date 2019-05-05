import time
import datetime
import json
import requests
import RPi.GPIO as io
import Adafruit_DHT
import math

from mfrc522 import SimpleMFRC522

def GetValueBoolean(pinAnalog,pinDigital):

    io.setmode(io.BCM)
    io.setup(pinAnalog,io.HIGH)
    io.setup(pinDigital,io.HIGH)

    valueAnalog = io.input(pinAnalog)
    valueDigital = io.input(pinDigital)

    Value = [valueAnalog, valueDigital]
    return Value

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

def GetTemp(pin):

    io.setmode(io.BCM)
    io.setup(pin,io.IN) # make pin into an output

    value = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin)

    return value

def RealTime(url):
    DateTime = datetime.datetime.now()
    URL = url

    headers = {
        'accept': 'application/json',
    }

    params = (
            ('date_time', DateTime.strftime("%Y-%m-%dT%H:%M:%S+08:00")),
            ('date', DateTime.date),
        ) #Unused

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        print(response)
        return None
    

def RFID(mode):
    reader = SimpleMFRC522()

    if mode == 'w':
        text = raw_input('New data:')
        print("Now place your tag to write")
        reader.write(text)
        print("Written")
    elif mode == 'r':
        id, text = reader.read()
        print(id)
        print(text)

    reader = None # w to write, r to read

def X(url):
    # Get airtemperature
    AirTemp = RealTime(url)


    # find number of stations available
    item = AirTemp['metadata']['stations']
    n_station = len(item)

    # Display the stations
    for i in range(0, n_station):
        item = AirTemp['metadata']['stations'][i]['name']
        #latitude = AirTemp['metadata']['stations'][i]['location']['latitude']
        #longitude = AirTemp['metadata']['stations'][i]['location']['longitude']
        print("({}) {}".format(i,item))

    #choice = input("Choose nearest station: ")

    # convert choice to station id
    stationID = AirTemp['metadata']['stations'][choice]['device_id']

    # get the temperature of the selected if
    for i in range(0, n_station):
        if AirTemp['items'][0]['readings'][i]['station_id'] == stationID:
            Temperature = AirTemp['items'][0]['readings'][i]['value']

    # Get unit
    Unit = AirTemp['metadata']['reading_unit']

    Value = [str(Temperature), Unit]
    return Value # Value = [X, Unit], 
               #  Where X = Temperature, Winddirection, Windspeed

def X2(url):
    # Get airtemperature
    AirTemp = RealTime(url)


    # find number of stations available
    item = AirTemp['metadata']['stations']
    n_station = len(item)

    # Get unit
    Unit = AirTemp['metadata']['reading_unit']

    # Display the stations
    for i in range(0, n_station):
        item = AirTemp['metadata']['stations'][i]['name']
        Temperature = AirTemp['items'][0]['readings'][i]['value']
        print("{} {} at {} station".format(Temperature, unit, item))

   


def UVlight():
    # Get UV reading
    UVreading = RealTime("https://api.data.gov.sg/v1/environment/uv-index")

    # Display the number of results
    item = UVreading['items'][0]['index']
    n = len(item)

    for i in range(0, n):
        item = UVreading['items'][0]['index'][i]['value']
        item2 = UVreading['items'][0]['index'][i]['timestamp']
        
        print("{} > UV are at {} level".format(item2, item))

#def Whatitfeelslike(temp, humidity):
#    e = 2.71828182845904
#    N = 0.6687451584
#    RH = humidity
#    Td = temp
    
#    ed = 6.112 * exp( (17.502 * Td) / (240.97 * Td) )
#    ew = 6.112 * exp( (17.502 * Tw) / (240.97 * Tw) )


def Main():
     while True:
         Rain = GetValueBoolean(20, 21) #rain sensor, 20 is analog, 21 is digital
         #Sound = GetValueBoolean(26, 19) #sound sensor, 26 is analog, 19 is digital
         TempAndHumidity = GetTemp(19)
         distance = GetDistance(23, 24) # Trig and echo
         TimeNow = datetime.datetime.now().time()
         print("\nRain Sensor  A:{}  D:{}".format(Rain[0],Rain[1]))
         #print("Sound Sensor A:{}  D:{}".format(Sound[0],Sound[1]))
         print("Temperature:{} Celius".format(TempAndHumidity[1]))
         print("Humidity: {}%".format(TempAndHumidity[0]))
         print("Distance: {} cm".format(distance))
         print("----{}s".format(TimeNow))
         time.sleep(5)






#-----------------------------------------------
#Main()
distance = GetDistance(24, 23) # Trig and echo
print(distance)

#print("TEMPERATURE")
#airtemp = X("https://api.data.gov.sg/v1/environment/air-temperature")
#print("Temperature is {} {}".format(airtemp[0], airtemp[1]))

#print("WIND DIRECTION")
#Winddirection = X("https://api.data.gov.sg/v1/environment/wind-direction")
#print("WindDirection is {} {}".format(Winddirection[0], Winddirection[1]))

#print("WIND SPEED")
#windspeed = X("https://api.data.gov.sg/v1/environment/wind-speed")
#print("Windspeed is {} {}".format(windspeed[0], windspeed[1]))


#UVlight()

#RFID('r')

io.cleanup()