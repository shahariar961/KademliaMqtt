import paho.mqtt.client as paho
import sys
import time
import asyncio
from kademlia.network import Server
import datetime
from dateutil.parser import parse
fileName="date.txt"
delimiter='='
file = open(fileName, 'r')
newDate=str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
def findValue(fullString):
    value= fullString[fullString.index(delimiter)+1:]
    value=value.replace(" ","")
    return value
for line in file:
    if line.startswith('date'):
        lastDate=findValue(line)
key= "key"
node="127.0.0.1"
port="8469"
async def run():
    server = Server()
    await server.listen(8473,interface="127.0.0.1")
    bootstrap_node = (node, int(port))
    await server.bootstrap([bootstrap_node])

    result = await server.get(key)
    print("Get result:", result)
    server.stop()
    topic,newDate=result.split()
    return topic,newDate

topic,newDate=asyncio.run(run())



parseLastDate=parse(lastDate)
parseNewDate=parse(newDate)

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

