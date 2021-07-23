import os 
import shutil
import time

thetime = time.strftime('%H:%M')
thedate = time.strftime('%m-%d-%y')
source = 'C:/Users/Paul/Downloads/123/'
destination = 'C:/Users/Paul/Downloads/456/'


print('Hello')
for filename in os.listdir(source):
    newsource = source + filename
    newdestination = destination + thedate + ' ' + filename
    print(newsource)
    print(newdestination)
    print()

print('end?')
input()
