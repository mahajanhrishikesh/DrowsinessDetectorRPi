import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

buzzer = 23
GPIO.setup(buzzer,GPIO.OUT)

print("Buzzer On!!")
GPIO.output(buzzer,GPIO.HIGH)
time.sleep(2)
GPIO.output(buzzer,GPIO.LOW)

