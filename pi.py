import RPi.GPIO as GPIO
import requests
import time

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up sensor GPIO
SMOKE_SENSOR_PIN = 17
FLAME_SENSOR_PIN = 27

# Set up Smoke and Flame sensor as input
GPIO.setup(SMOKE_SENSOR_PIN, GPIO.IN)
GPIO.setup(FLAME_SENSOR_PIN, GPIO.IN)


def detect_fire():
    smoke = GPIO.input(SMOKE_SENSOR_PIN)
    flame = not GPIO.input(
        FLAME_SENSOR_PIN
    )  # Flame sensor gives 0 when flame is detected

    if smoke == 1 or flame:
        response = requests.get("http://www.example.com/detected")
        print("Fire detected! Response:", response.text)


while True:
    detect_fire()
    time.sleep(1)
