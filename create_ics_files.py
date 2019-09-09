from icalendar import Calendar, Event
import json
import dateutil.parser

# this calendar will have all of the events
the_everything_calendar = Calendar()
the_everything_calendar.add("prodid", "-//HashiConf2019//mxm.dk//")
the_everything_calendar.add("version", "2.0")

for event_json in json.load(open("schedule.json")):
    one_time_calendar = Calendar()
    one_time_calendar.add("prodid", f"-//{event_json['title']}//mxm.dk//")
    one_time_calendar.add("version", "2.0")

    event = Event()
    event.add("summary", event_json["title"])

    event.add("dtstart", dateutil.parser.parse(event_json["start_time"]))
    event.add("dtend", dateutil.parser.parse(event_json["end_time"]))

    one_time_calendar.add_component(event)
    f = open(f"ics_files/{event_json['title']}.ics", "wb")
    f.write(one_time_calendar.to_ical())
    f.close()

    the_everything_calendar.add_component(event)

f = open(f"ics_files/THE_ENTIRE_HASHICONF_SCHEDULE_2019.ics", "wb")
f.write(the_everything_calendar.to_ical())
f.close()
