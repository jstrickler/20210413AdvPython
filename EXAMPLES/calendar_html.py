#!/usr/bin/env python

import os
import calendar
import webbrowser

hcal = calendar.HTMLCalendar()  # <1>
formatted_month = hcal.formatmonth(2021, 4)  # <2>
print(formatted_month)

html_file_name = 'sample_calendar.html'

with open(html_file_name, 'w') as calendar_out:
    calendar_out.write(formatted_month)  # <3>
    webbrowser.open("file://" + os.path.realpath(html_file_name))  # <4>

print("html_file_name: {}\n".format(html_file_name))

# "Wombats Unlimited!"
