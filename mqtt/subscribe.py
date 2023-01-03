import paho.mqtt.client as paho
import sys
import time

def onMessage(client,userdata,msg):
    print(msg.topic + ":" + msg.payload.decode())

client=paho.Client("p2",clean_session=False)
client.on_message=onMessage
if client.connect("localhost",1883,60) !=0:
    print("Could not connect")
    sys.exit(-1)

client.subscribe("test")

try:
    client.loop_start()
except:
    print("Disconnect")
time.sleep(2)
client.disconnect()
