import speedtest
import time
import datetime


s = speedtest.Speedtest()

time_now = datetime.datetime.now().strftime("%H:%M:%S")
downspeed = round((round(s.download()) / 1048576), 2)
upspeed = round((round(s.upload()) / 1048576), 2)

while True:
    print(f"time: {time_now}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")
    time.sleep(5)