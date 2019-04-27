# IoT Room humidity control using ESP32, DHT22 and Adafruit IO

------------------Latest-------------------------------
--------------------------------------------------------
## Introduction

After learning about how to connect Raspberry Pi and ESP32 via MQTT, I stumbled upon another very interesting Github user @DaveSprague who connected the ESP8266 directly to Adafruit IO. This is interesting as it frees my Raspberry Pi for other interesting projects. So I decided this is the way to go. 

## Problem statement
At this point of time it will be worth noting the "real" purpose of this project. I live in Germany where the weather is brutally dry for an Indian like me. My daughter has dry skin problems which got me thinking to start monitorinng the humidity in our house. I found that at times, the humidity can reach well below 30%. According to a quick google research, the average indoor humidity, comfortable for humans, should be between 30%-60%. This is not good and I decided to buy a humidifier for her room. 

The problem with humidifier is that we cant monitor how much is the humidity and or the impact of humidifier after its switched on. 
For this I decided to build this very simple project. 

## Disclaimer
The code is taken directly from @DaveSprague with very few modification. So a special thanks for Dave for providingn the code and explanation on his Github page: 
https://github.com/openhomeautomation/adafruit-io-esp8266/blob/master/esp8266_sensor_module/esp8266_sensor_module.ino

## Pictures from the project
### The hardware used:
![](Images/Hardware%sRequirements.jpg)

### ESP32 Front
![](Images/ESP32.jpg)

### ESP32 Back connections
![](Images/ESP32 connection.jpg)






# check the contributor link
# add issues faced during the project
# check fromatting for markdown


--------------------------------------------------------
-------------------OLD----------------------------------
This Repo is for my project to learn about MQTT protocol, use Raspberry Pi and ESP32 chip to transmit, wirelessly, humidity and temp sensor from DHT22.

The end game is to control my humidifier based on humidity values, for which I am currently thinking of using IFTT and a smart electric plug to which the humidifier will be connected.

The project is heavily influenced by the steps shared by rotoron in his website: 
https://www.rototron.info/raspberry-pi-esp32-micropython-tutorial/ 
-------------------------------------------------------
