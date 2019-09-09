import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED = 29

GPIO.setup(LED, GPIO.OUT)

GPIO.output(LED, True)

time.sleep(5)

GPIO.output(LED, False)
