import RPi.GPIO as GPIO
import time
import serial

# --- Configuration ---
PIR_PIN = 17
NO_MOTION_THRESHOLD = 10  # seconds
LORA_PORT = '/dev/ttyS0'
BAUD_RATE = 9600
SOLDIER_ID = "#IND-0457"

# --- Setup ---
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

ser = serial.Serial(LORA_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # Allow time for LoRa module to initialize

last_motion_time = time.time()
sos_triggered = False

try:
    print("Monitoring started...")
    while True:
        motion = GPIO.input(PIR_PIN)

        if motion:
            print("Motion detected!")
            last_motion_time = time.time()
            sos_triggered = False

        elif time.time() - last_motion_time > NO_MOTION_THRESHOLD and not sos_triggered:
            sos_message = f"SOS: No motion detected from {SOLDIER_ID}"
            print(sos_message)
            ser.write(sos_message.encode())
            sos_triggered = True

        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting program...")

finally:
    GPIO.cleanup()
    ser.close()
