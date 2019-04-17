'''
import network
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect("username","password")
'''

import ConnectWifi

ConnectWifi.connect()

import dht_publish
