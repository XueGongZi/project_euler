# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

def timeConversion(s):
    hr, form, time = s[:2], s[-2:], s[2:-2]
    initial_time, mid_time = "00", "12"
    am, pm = "AM", "PM"
    if hr == mid_time and form == am:
        return initial_time + time
    elif hr != mid_time and form == "PM":
        return str(int(hr) + 12) + time
    else:
        return s[:-2]
