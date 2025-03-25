import sys
import os
import datetime
import time
import pytz
sys.path.append('./')
from Collective_resources.sevseg import Display

TIME_ZONE = 'Asia/Kolkata'

display = Display([0,0,0])

while True:
    try:
        now = datetime.datetime.now().astimezone(pytz.timezone(TIME_ZONE))
        os.system('cls' if os.name == 'nt' else 'clear')
        present_time = [now.hour,now.minute,now.second]
        display.set_display(present_time)
        print(''.center(27,'_'))
        print('Digital Clock'.center(27,'_'))
        print(display)
        print(''.center(27,'_'))
        print('Press ctrl+C to quit'.center(27,'_'))
        time.sleep(1)
    except KeyboardInterrupt:
        print('\nExiting...')
        exit(0)