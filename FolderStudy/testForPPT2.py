import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
R,G,B=15,18,14
GPIO.setmode(GPIO.BCM)

GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)

pwmR=GPIO.PWM(R,10)
pwmG=GPIO.PWM(G,1)
pwmB=GPIO.PWM(B,1)

pwmR.start(50)
pwmG.start(50)
pwmB.start(50)



time.sleep(5)

pwmR.stop()
pwmG.stop()
pwmB.stop()

GPIO.cleanup()