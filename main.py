import config
from sensor_utils import *
from network_utils import *

# Pins and sensors setup
dht_pin = Pin(0)
soil_power_pin = Pin(15, Pin.OUT)
soil_analog = ADC(26)
d_internal = DHT11(dht_pin)
server_url = f"{config.base_url}{config.api_url}"

def main() -> None:
    wlan = connect_to_wifi(config.ssid, config.password)
    try:
        while True:
            # ping_google()
            temp, humidity = read_dht_sensor(d_internal)
            moisture = read_soil_moisture(soil_power_pin, soil_analog)
            data = {
                "temperature": temp,
                "humidity": humidity,
                "moisture": moisture
            }
            try:
                send_data(server_url, data)
            except Exception as e:
                print("Failed to send data:", e)
            sleep(2)
    except KeyboardInterrupt:
        wlan.disconnect()
        wlan.active(False)
        soil_power_pin.value(0)
        print("Stopped.")

main()