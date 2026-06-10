#This main.py is for the beacon esp32 board

import network
import time

#Initialize the Access Point interface
ap = network.WLAN(network.AP_IF)

#Name of first test location
SSID = "Kitchen_Test"
PASSWORD = "password123"

#Network protocall details
ap.config(essid=SSID, password=PASSWORD, authmode=network.AUTH_WPA2_PSK)
ap.active(True)

print(f"--- BEACON ACTIVE: Broadcasting '{SSID}' ---")

while True:
    time.sleep(1)