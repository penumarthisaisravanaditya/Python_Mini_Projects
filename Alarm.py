import time
from datetime import datetime

alarm_time = input("Set the alarm time(HH:MM):")

print("Alarm set for:", alarm_time)
while True:
    current_time = datetime.now().strftime("%H:%M")
    if current_time == alarm_time:
        print("Alarm! Wake up!")
        break
    time.sleep(1)