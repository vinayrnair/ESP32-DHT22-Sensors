from time import sleep
from umqtt.simple import MQTTClient
from machine import Pin
from dht import DHT22

SERVER = 'ip address'  # MQTT Server Address (Change to the IP address of your Pi)
CLIENT_ID = 'ESP32_DHT22_Sensor'
TOPIC = b'temp_humidity'

client = MQTTClient(CLIENT_ID, SERVER)
client.connect()   # Connect to MQTT broker

sensor = DHT22(Pin(23, Pin.IN, Pin.PULL_UP))   # DHT-22 on GPIO 23 (input with internal pull-up resistor)

while True:
    try:
        sensor.measure()   # Poll sensor
        t = sensor.temperature()
        h = sensor.humidity()
        if isinstance(t, float) and isinstance(h, float):  # Confirm sensor results are numeric
            msg = (b'{0:3.1f},{1:3.1f}'.format(t, h))
            client.publish(TOPIC, msg)  # Publish sensor data to MQTT topic
            print(msg)
        else:
            print('Invalid sensor readings.')
    except OSError:
        print('Failed to read sensor.')
    sleep(4)
