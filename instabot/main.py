import time
from instabot_old import add_like
import sys

# Numero like al giorno 150
# Max 15/ora
#cyclinglife
#roadbike
#bicycle 
#cyclist

def check(hashtag):
    file_name = './output_' + str(time.localtime().tm_mday) + '.txt'
    # sys.stdout = open(file_name, 'w')
    print('-------------------------------------------TASK RUN @------------------------------------------------')
    print('Day:', time.localtime().tm_mday, '/', time.localtime().tm_mon, '\n')
    print('Time:', time.localtime().tm_hour, ':', time.localtime().tm_min, ':', time.localtime().tm_sec, '\n')
    add_like(hashtag)
    # sys.stdout.close()

counter = 0
while counter<50:
    try:
        check('#cyclinglife')
        time.sleep(60*1)
        check('#roadbike')
        time.sleep(60*1)
        check('#bicycle')
        time.sleep(60*1)
        check('#cyclist')
        time.sleep(60*1)

        counter = counter + 1

    except Exception as e:
        print(e)


