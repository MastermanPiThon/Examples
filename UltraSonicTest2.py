from SonicSensor import *

sensor = SonicSensor ("banana", 23, 24)

count = 0
while True:
    print ("{} Distance inches: {}".format (count, sensor.PingInch ()))
    count += 1
