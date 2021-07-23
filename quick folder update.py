import os 
import shutil
import time
import magic

source = 'C:/Users/Paul/Music/fresh-oil-moments-november-2020/Resting Place - Fresh Oil Moments - November 2020/'

for filename in os.listdir(source):
    os.rename(source + filename, source +  'Fresh Oil Moments - November 2020 - Resting Place - ' + filename)
