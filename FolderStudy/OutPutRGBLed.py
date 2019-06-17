import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
R,G,B=14,15,18
GPIO.setmode(GPIO.BCM)

GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)

pwmR=GPIO.PWM(R,1)
pwmG=GPIO.PWM(G,1)
pwmB=GPIO.PWM(B,1)

pwmR.start(0)
pwmG.start(0)
pwmB.start(0)

t = 0.4
a = 0
while a < 5:
    a+=1
    pwmR.ChangeDutyCycle(0)
    pwmG.ChangeDutyCycle(100)
    pwmB.ChangeDutyCycle(100)
    time.sleep(t)
        
    
    pwmR.ChangeDutyCycle(100)
    pwmG.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(100)
    time.sleep(t)
        

    pwmR.ChangeDutyCycle(100)
    pwmG.ChangeDutyCycle(100)
    pwmB.ChangeDutyCycle(0)
    time.sleep(t)
        
    pwmR.ChangeDutyCycle(0)
    pwmG.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(100)
    time.sleep(t)
        

    pwmR.ChangeDutyCycle(0)
    pwmG.ChangeDutyCycle(100)
    pwmB.ChangeDutyCycle(0)
    time.sleep(t)
        

    pwmR.ChangeDutyCycle(100)
    pwmG.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(0)
    time.sleep(t)
        
    pwmR.ChangeDutyCycle(0)
    pwmG.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(0)
    time.sleep(t)
        

    for r in range (0, 101, 20):
        pwmR.ChangeDutyCycle(r)
        for g in range (0, 101, 20):
            pwmG.ChangeDutyCycle(g)
            for b in range (0, 101, 20):
                pwmB.ChangeDutyCycle(b)
                time.sleep(0.01)


pwmR.stop()
pwmG.stop()
pwmB.stop()

GPIO.cleanup()