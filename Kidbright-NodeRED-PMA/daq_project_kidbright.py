
from machine import Pin, I2C, ADC, PWM
from math import log10
import network
import time
from umqtt.robust import MQTTClient

from config import (
  WIFI_SSID, WIFI_PASS,
  MQTT_BROKER, MQTT_USER,
  MQTT_PASS
)
import uasyncio as asyncio
import json
import kidbright as kb
import dht


PUB_MQTT_TOPIC = "b6510545306/clothesdrying"
TOPIC_LAMP = "b6510545306/lamp"

ain = ADC(Pin(36))
i2c = I2C(1, sda=Pin(4), scl=Pin(5))

lamp = Pin(25, Pin.OUT)
lamp.value(1)

kb.init()

led_wifi = Pin(2, Pin.OUT)
led_wifi.value(1) # turn the red led off
led_iot = Pin(12, Pin.OUT)
led_iot.value(1)  # turn the green led off


# WIFI Connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_SSID, WIFI_PASS)
while not wlan.isconnected():
  time.sleep(0.5)
led_wifi.value(0) # turn the red led on
print("---> Connected to WIFI")

# MQTT Connection
mqtt = MQTTClient(client_id="",
         server=MQTT_BROKER,
         user=MQTT_USER,
         password=MQTT_PASS)
mqtt.connect()
led_iot.value(0)  # turn the green led on
print("---> Connected to MQTT")


async def publish_primary_data():
  while True:
    dht11 = dht.DHT11(Pin(32))
    dht11.measure()  
    data = {"lat": 13.850432420329991,
        "lon": 100.60571194293834,
        "light": kb.light(),
        "temperature": dht11.temperature(),
        "humidity": dht11.humidity()}
    print(data)
    mqtt.publish(topic=PUB_MQTT_TOPIC, msg=json.dumps(data))
    await asyncio.sleep(600)
     
def lamp_on_off_online(topic, payload):
  # use decode instead of direct byte-array comparison
  if topic.decode() == TOPIC_LAMP:
    print(int(payload))
    try:
      lamp.value(1-int(payload))
       
    except ValueError:
      pass
       
async def check_mqtt():
  while True:
    mqtt.check_msg()
    await asyncio.sleep_ms(0)
     
async def check_alive():
  while True:
    await asyncio.sleep(10)
    checker = "alive"
    mqtt.publish(topic="b6510545306/checker", msg=checker)
    print("alive")

#mqtt.set_callback(lamp_on_off_online)
#mqtt.subscribe(TOPIC_LAMP)
asyncio.create_task(publish_primary_data())
asyncio.create_task(check_mqtt())
asyncio.create_task(check_alive())
asyncio.run_until_complete()