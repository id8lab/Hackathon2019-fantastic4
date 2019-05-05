#Program to run HC-SR04 Sensor connected by Breadboard
import RPi.GPIO as GPIO
import time

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

GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIG_PIN,GPIO.OUT)
GPIO.setup(ECHO_PIN,GPIO.IN)
try:

    while True:
        GPIO.output(TRIG_PIN,True)
        time.sleep(0.0001)
        GPIO.output(TRIG_PIN,False)

        while GPIO.input(ECHO_PIN)== False:
            start=time.time()
        while GPIO.input(ECHO_PIN)==True:
            stop=time.time()

        distance = (stop-start)*(34200/2)
        print("Distance in cm is :", distance)

        time.sleep(1)

except (KeyboardInterrupt):
    print("Program Halted by Ctrl-C")

GPIO.cleanup()

