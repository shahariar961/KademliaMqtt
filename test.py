import datetime
import random
import sys
import paho.mqtt.client as paho
import time
from dateutil.parser import parse
# fileName="test.txt"
# delimiter='='
# file = open(fileName, 'r')
# def findValue(fullString):
#     value= fullString[fullString.index(delimiter)+1:]
#     value=value.replace(" ","")
#     return value
# for line in file:
#     if line.startswith('date'):
#         date3=findValue(line)

# print(date3)
# date4="date="+str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

# with open(fileName,'w') as f:
#     f.write(date4)

# date=str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

# # date2="20230104154532"
# date9=""
# parsedate=parse(date)
# parsedate2=parse(date9)
# print(parsedate)
# print(parsedate)
# if parsedate<parsedate2:
#     print('yes')

client=paho.Client("p1")
date=str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
if client.connect("localhost",1883,600) !=0:
    print("Could not connect")
    sys.exit(-1)
proximity=str(random.randint(1000,2000))
message=proximity + " "+ date
client.publish("test",message,qos=1,retain=True)
print("published")
print(message)
client.disconnect()

def onMessage(client,userdata,msg):
    print(msg.topic + ":" + msg.payload.decode())
    with open('file.txt','w') as r:
        r.write("New Content") 



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