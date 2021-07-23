import os 
import shutil
import time

thetime = time.strftime('%H:%M')
thedate = time.strftime('%m-%d-%y')
source = 'C:/Users/Paul/Downloads/123/'
destination = 'C:/Users/Paul/Downloads/456/'

print('The time is ' + thetime)
print('Today is ' + thedate)
print('Hello')
myresponse = input()
print(myresponse)
print('press enter to start')
input()

for filename in os.listdir(source):
    newsource = source + filename
    newdestination = destination + thedate + ' ' + filename
    os.rename(newsource, newdestination)
