import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
Button=14
LED=15
GPIO.setmode(GPIO.BCM)

GPIO.setup(Button, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

GPIO.output(LED,GPIO.LOW)
count=0
while( count <= 1000):
    buttonStatus=GPIO.input(Button)
    if(GPIO.input(Button)==0):
        GPIO.output(LED,GPIO.HIGH)
    else:
        GPIO.output(LED,GPIO.LOW)
    count+=1
    time.sleep(0.01)
GPIO.cleanup()