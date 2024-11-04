import network
from socket import socket, getaddrinfo
from time import sleep

def connect_to_wifi(ssid: str, password: str) -> network.WLAN:
    """Connect to Wi-Fi using provided SSID and password."""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.disconnect()
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        sleep(1)
    print("Connected to Wi-Fi")
    print("Network config:", wlan.ifconfig())
    return wlan

def ping_google():
    try:
        addr = getaddrinfo('www.google.com', 80)[0][-1]
        s = socket()
        s.connect(addr)
        print("Connected to Google - Internet connection is up.")
        s.close()
    except OSError as e:
        print("Unable to connect to Google:", e)