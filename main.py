import config
from sensor_utils import *
from network_utils import *

# Pins and sensors setup
dht_pin = Pin(0)
pump_relay_pin = Pin(28, Pin.OUT)
soil_power_pin = Pin(15, Pin.OUT)
soil_analog = ADC(26)
d_internal = DHT11(dht_pin)

def main() -> None:
    wlan = connect_to_wifi(config.ssid, config.password)
    try:
        while True:
            # ping_google() # - for testing network connection
            temp, humidity = read_dht_sensor(d_internal)
            moisture = read_soil_moisture(soil_power_pin, soil_analog)
            activate, seconds = get_pump_command()
            print(f"Activate {activate}")
            print(f"Seconds {seconds}")
            if activate:
                activate_relay(pump_relay_pin, int(seconds))
            sleep(1)
            data = {
                "temperature": temp,
                "moisture": moisture,
                "humidity": humidity,
                "device_id": config.device_id
            }
            print(data)
            try:
                send_data(f"{config.base_url}{config.api_url}{config.data_endpoint}", data)
            except Exception as e:
                print("Failed to send data:", e)
            sleep(5)
            
    except Exception as e:
        print(e)
        wlan.disconnect()
        wlan.active(False)
        soil_power_pin.value(0)
        pump_relay_pin.value(0)
        print("Stopped.")

main()