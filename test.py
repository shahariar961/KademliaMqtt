import datetime
from dateutil.parser import parse
fileName="test.txt"
delimiter='='
file = open(fileName, 'r')
def findValue(fullString):
    value= fullString[fullString.index(delimiter)+1:]
    value=value.replace(" ","")
    return value
for line in file:
    if line.startswith('date'):
        date3=findValue(line)

print(date3)
date4="date="+str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

with open(fileName,'w') as f:
    f.write(date4)

date=str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

# date2="20230104154532"
date9=""
parsedate=parse(date)
parsedate2=parse(date9)
print(parsedate)
print(parsedate)
if parsedate<parsedate2:
    print('yes')