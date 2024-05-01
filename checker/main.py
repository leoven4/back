import time
from notifier import notify_via_email
from check_webpage import check_webpage
import sys
sys.stdout = open('./output.txt', 'w')
counter = 0

def check():
    print('-------------------------------------------TASK RUN @------------------------------------------------')
    print('Day:', time.localtime().tm_mday, '/', time.localtime().tm_mon, '\n')
    print('Time:', time.localtime().tm_hour, ':', time.localtime().tm_min, ':', time.localtime().tm_sec, '\n')
    check_webpage()


while counter<24:
    try:
        check()
        time.sleep(60*30)
        counter = counter + 1

    except Exception as e:
        print(e)
        notify_via_email('', 'Error in pycode')

sys.stdout.close()

