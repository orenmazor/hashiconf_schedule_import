# What is this

The HashiConf schedule is a javascript powered page located here: https://hashiconf.hashicorp.com/schedule?day=2

I wanted this conveniently in my google calendar.

# how this works

This script requires access to your google account. It's a mostly direct copy of the quickstart.py from https://developers.google.com/calendar/quickstart/python.

Because the schedule page is javascript powered, I couldn't just pull the page into BeautifulSoup (which doesnt read javascript). Instead I manually opened each page in inspector, forced the day, and saved the output html into this repo. Not great. Not terrible.

# Usage

1. Do not commit the token.pickle file or your credentials.json.
2. OPTIONAL: If you think the schedule changed, you will need to manually save the html into the *.html files. I'm gonna assume the schedule wont just change, or you'll see a lot of stressed out Hashiconf employees around.
3. Go to https://developers.google.com/calendar/quickstart/python and follow step 1 to generate a credentials.json file for yourself. It'll look like mine, but that one'll be yours. 
4. Run `python run_me.py`. It will do the auth bounce and grant access to this app to your google calendar. It'll then read the schedule.json file and create events.

# Note

I am not responsible for anything, ever. This code is [WTFPL](http://www.wtfpl.net/about/)
