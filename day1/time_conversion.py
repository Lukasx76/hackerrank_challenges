"""
    Problem: Given a time in -hour AM/PM format, convert it to military (24-hour) time.
    Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
    - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
"""

from datetime import datetime

def timeConversion(s):
    # converting string to datetime
    converted_string = datetime.strptime(s, "%I:%M:%S%p")

    # returning just the string
    return converted_string.strftime("%H:%M:%S")


print(timeConversion("07:05:45PM"))