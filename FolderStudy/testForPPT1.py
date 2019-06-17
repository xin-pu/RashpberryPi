import RPi.GPIO as GPIO
import time
import smbus  

address = 0x48 
GPIO.setwarnings(False)
R,G,B=14,15,18
Button=4
GPIO.setmode(GPIO.BCM)

GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
bus = smbus.SMBus(1) 
test=0x40

i=0
while i<100:
    bus.write_byte(address,test)  
    value = bus.read_byte(address) 
    print(value)
    i=i+1
    if value>122:
        GPIO.output(R,GPIO.HIGH)
        GPIO.output(G,GPIO.LOW)
        GPIO.output(B,GPIO.LOW)
    else:
        GPIO.output(R,GPIO.LOW)
        GPIO.output(G,GPIO.HIGH)
        GPIO.output(B,GPIO.LOW)
    time.sleep(0.1)
GPIO.cleanup()


