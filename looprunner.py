#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import pyrebase
from datetime import datetime
firebaseConfig = {
    'apiKey': "AIzaSyD-nqdhZtiIol5psI1_BkIwMAAa3keOX9I",
    'authDomain': "data-8889a.firebaseapp.com",
    'databaseURL': "https://data-8889a.firebaseio.com",
    'projectId': "data-8889a",
    'storageBucket': "data-8889a.appspot.com",
    'messagingSenderId': "489236791138",
    'appId': "1:489236791138:web:caaf218e465375eb"
}

try:
    GPIO.setmode(GPIO.BOARD)

    PIN_TRIGGER = 16
    PIN_ECHO = 18

    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    print("Waiting for sensor to settle")

    time.sleep(2)

    while(True):

        print("Calculating distance")

        GPIO.output(PIN_TRIGGER, GPIO.HIGH)

        time.sleep(0.00001)

        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(PIN_ECHO) == 0:
            pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO) == 1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        print("Distance:", distance, "cm")
        firebase = pyrebase.initialize_app(firebaseConfig)
        db = firebase.database()
        now = datetime. now()
        alfa = distance
        timestamp = datetime. timestamp(now)
        data = {
            "cap": "50", "fil": alfa, "lastupdate": str(int(timestamp))
        }
        results = db.child("Bin1").set(data)

        time.sleep(1)

finally:
    GPIO.cleanup()
