# Flower Watering System

This project is an IoT-based flower watering system using a Raspberry Pi Pico W.

## Features

- Monitors soil moisture, temperature, and humidity levels.
- Sends sensor data to a cloud server for tracking and logging.
- Designed for automation in watering systems based on soil moisture levels.

## Hardware Requirements

- **Raspberry Pi Pico W**
- **Soil Moisture Sensor** (e.g., HiLetgo LM393 3.3V-5V)
- **DHT11 Temperature & Humidity Sensor**
- **Water pump**
- **Wi-Fi Access**

## Folder Structure

```plaintext
project-folder/
│
├── main.py                # Main script for the watering system
├── sensor_utils.py        # Utility functions for sensor readings and data sending
├── network_utils.py       # Utility functions for Wi-Fi connection
└── config.py              # Configuration file with Wi-Fi and server details
