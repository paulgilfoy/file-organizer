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
    newfilename = thedate + ' ' + filename
    print(filename)
    print(newfilename)
    print()
    try :
        print(magic.from_file(source + filename, mime=True))
        if 'video' in magic.from_file(source + filename, mime=True):
            os.rename(source + filename, destvid + newfilename)
        elif 'image' in magic.from_file(source + filename, mime=True):
            os.rename(source + filename, destpic + newfilename)
        elif 'audio' in magic.from_file(source + filename, mime=True):
            os.rename(source + filename,destmusic + newfilename)
        elif 'docx' in filename : 
            os.rename(source + filename, destdoc + newfilename)
        elif 'pdf' in filename :
            os.rename(source + filename, destdoc + newfilename)
        elif 'torrent' in filename :
            os.rename(source + filename, destvid + newfilename)
        elif 'application' in magic.from_file(source + filename, mime=True):
            print('Leaving file alone')
        else : 
            print('none of these worked')
            print('...')
    except PermissionError:
        print()
    print()

