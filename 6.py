import os 
import shutil
import time
import magic

thetime = time.strftime('%H:%M')
thedate = time.strftime('%y-%m-%d')
source = 'C:/Users/Paul/Downloads/'
destvid = 'C:/Users/Paul/Videos/'
destdoc = 'C:/Users/Paul/Documents/'
destpic = 'C:/Users/Paul/Pictures/'
destmusic = 'C:/Users/Paul/Music/'

print('The time is ' + thetime)
print('Today is ' + thedate)
print('Hello')
myresponse = input()
print(myresponse)
print('press enter to start')
input()

for filename in os.listdir(source):
    testingfilename = thedate + ' ' + filename
    print(filename)
    print(testingfilename)
    print()
    try :
        print(magic.from_file(source + filename, mime=True))
        if 'video' in magic.from_file(source + filename, mime=True) == True :
            print(destvid + testingfilename)
        elif 'image' in magic.from_file(source + filename, mime=True) == True :
            print(destpic + testingfilename)
        elif 'application' in magic.from_file(source + filename, mime=True) == True :
            print('Leaving file alone')
        elif 'music' in magic.from_file(source + filename, mime=True) == True :
            print(destmusic + testingfilename)
        else :
            print('none of these worked')
            print('...')
    except PermissionError:
        print()
    print()

