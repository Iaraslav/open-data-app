import network
import config
from socket import socket, getaddrinfo
from time import sleep
import urequests

def connect_to_wifi(ssid: str, password: str) -> network.WLAN:
    """Connect to Wi-Fi using provided SSID and password."""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.disconnect()
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print("Connecting to Wi-FI")
        sleep(5)
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

def get_pump_command() -> tuple[bool, int]:
    """Retrieve `activate` and `seconds` variables from the server for the `activate_relay` function"""
    try:
        print(f'{config.base_url}{config.api_url}{config.command_endpoint}')
        response = urequests.get(f'{config.base_url}{config.api_url}{config.command_endpoint}')
        data = response.json()
        response.close()
        activate = data.get('activate', False)
        seconds = data.get('seconds', 0)
        return activate, seconds
    except Exception as e:
        print("Error checking server:", e)
        return False, 0