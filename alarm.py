
''' Alarm using python'''
from playsound import playsound
from datetime import datetime
import os
alarm_time = "19:22:35"
alarm_hour = alarm_time[0:2]
alarm_minutes = alarm_time[3:5]
alarm_second = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print(alarm_hour,alarm_minutes,alarm_second,alarm_period)
# print(os.getcwd()+ str("\song.mp3"))

while True:
    now=datetime.now()
    current_hour = now.strftime("%H")
    current_minute = now.strftime("%M")
    current_second = now.strftime("%S")
    current_period = now.strftime("%p")
    print(current_period)
    if current_hour==alarm_hour:
        if current_minute==alarm_minutes:
            if current_second==alarm_second:
                print("Wakd up..")

                playsound(os.getcwd()+ str("\song.mp3"))
                break