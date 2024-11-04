from machine import Pin, ADC
from time import sleep
import urequests
from dht import DHT11

def read_soil_moisture(soil_power_pin: Pin, soil_analog: ADC) -> int:
    """Read soil moisture level as a percentage."""
    soil_power_pin.value(1)
    sleep(0.5)
    moisture_analog = soil_analog.read_u16()
    soil_power_pin.value(0)
    return round(((65535 - moisture_analog) / 65535) * 100)

def read_dht_sensor(d_internal: DHT11) -> tuple[int, int]:
    """Measure and return temperature and humidity from the DHT11 sensor."""
    d_internal.measure()
    return d_internal.temperature(), d_internal.humidity()

def send_data(url: str, data: dict[str, int]) -> None:
    """Send data to the server using a POST request."""
    headers = {"Content-Type": "application/json"}
    response = urequests.post(url, json=data, headers=headers)
    response.close()