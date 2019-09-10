import json
import dateutil.parser

from bs4 import BeautifulSoup
from datetime import timedelta

base_filename = "schedule_day_{}.html"
timestamps = ["2019-09-09", "2019-09-10", "2019-09-11"]
events = []

for day in range(0, 3):

    soup = BeautifulSoup(open(base_filename.format(day)), "html.parser")

    for raw_item in soup.select("div.schedule-items li"):

        # YOLO
        time = raw_item.select("span.time")[0].text
        if "AM" in time:
            time = time.replace("AM", "").strip()
            hour = int(time.split(":")[0])
            if hour < 10:
                time = "0" + time
        elif "PM" in time:
            time = time.replace("PM", "").strip()
            hour = time.split(":")[0]
            minutes = time.split(":")[1]
            if hour != "12":
                hour = int(hour) + 12

            time = f"{hour}:{minutes}"

        start_time = f"{timestamps[day]}T{time}:00-08:00"
        end_time = (dateutil.parser.parse(start_time) + timedelta(hours=1)).isoformat()

        event = {
            "title": raw_item.select("span.title")[0].text,
            "day": timestamps[day],
            "start_time": start_time,
            "end_time": end_time,
            "location": raw_item.select("span.location")[0].text,
        }
        print(start_time + " - " + event["title"])

        events.append(event)


with open("schedule.json", "w") as schedule_file:
    schedule_file.write(json.dumps(events))
