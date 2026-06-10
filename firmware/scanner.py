#This main.py is for the receiver esp32 board

import network
import time

#Initialize the wifi station (reciever) interface
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

#Target SSID we are looking for
TARGET_SSID = "Kitchen_Test"

print("Timestamp(s), SSID, RSSI")
start_time = time.time()

while True:
    #Scan the airwaves (returns a list of tuples with network info)
    networks = wlan.scan()
    
    current_time = time.time() - start_time
    found = False
    
    for net in networks:
        ssid = net[0].decode('utf-8', 'ignore')
        rssi = net[3] #Index 3 holds the Signal Strength (RSSI)
        
        if ssid == TARGET_SSID:
            #print data in clean csv format: time, name, signal strength
            print(f"{current_time:.1f},{ssid},{rssi}")
            found = True
            break
        
    if not found:
            #if the board temporarily loses the signal. log a blank/low value
        print(f"{current_time:.1f},{TARGET_SSID},None")
    
    #pause for half a second before scanning again
    time.sleep(0.5)