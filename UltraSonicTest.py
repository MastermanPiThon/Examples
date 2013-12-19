import time
import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BCM)

Trigger1 = 23
Echo1    = 24

print ("Setting Up GPIO")

GPIO.setup (Trigger1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup (Echo1,    GPIO.IN)

time.sleep (0.5)

count = 0
while True:
    GPIO.output (Trigger1, GPIO.HIGH)
    time.sleep (0.00009)
    GPIO.output (Trigger1, GPIO.LOW)

    start = time.time ()
    while GPIO.input (Echo1) == GPIO.LOW:
        start = time.time ()


    while GPIO.input (Echo1) == GPIO.HIGH:
        stop = time.time ()

    elapsedTime = stop - start

    distance = elapsedTime * 17000

    print ("{} Distance {} cm".format (count, distance))

    count += 1
