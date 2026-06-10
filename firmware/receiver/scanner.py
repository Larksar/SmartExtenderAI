import network
import time

#Initialize the wifi station (reciever) interface
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

#Target SSID we are looking for
TARGET_SSID = "Kitchen_Test"

LOCATION = "Kitchen"
RUN_ID = "run_01"
DURATION_SECONDS = 600 #10 mins
SCAN_DELAY = 1 #seconds between scans

print("scan_id,timestamp_s,location,run_id,ssid,channel,rssi,found")

start_time = time.time()
scan_id = 0

while time.time() - start_time < DURATION_SECONDS:
    scan_id += 1
    current_time = time.time() - start_time
    
    networks = wlan.scan()
    found = False
    
    for net in networks:
        ssid = net[0].decode("utf-8", "ignore")
        channel = net[2]
        rssi = net[3]
        
        if ssid == TARGET_SSID:
            print(f"{scan_id},{current_time:.1f},{LOCATION},{RUN_ID},{ssid},{channel},{rssi},1")
            found = True
            break
    
    if not found:
        print(f"{scan_id},{current_time:.1f},{LOCATION},{RUN_ID},{TARGET_SSID},None,None,0")
        
    time.sleep(SCAN_DELAY)
    
print("TEST COMPLETE")