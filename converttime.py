def convert_time(utc_time):
    # Split the time and timezone
    time_part, tz_part = utc_time[:-3], utc_time[-3:]
    # Split the time into hours, minutes, seconds and milliseconds
    hours, minutes, seconds = time_part.split(':')
    seconds, milliseconds = seconds.split('.')
    # Convert the timezone to an integer
    tz_offset = int(tz_part)

    # Adjust the time based on the timezone offset
    total_minutes = int(minutes) + tz_offset * 60
    total_hours = int(hours) + total_minutes // 60
    total_minutes %= 60
    total_hours %= 24

    # Round the milliseconds
    milliseconds = round(float('0.' + milliseconds) * 1000)
    # Adjust seconds, minutes, and hours if necessary
    total_seconds = int(seconds) + milliseconds // 1000
    milliseconds %= 1000
    total_minutes += total_seconds // 60
    total_seconds %= 60
    total_hours += total_minutes // 60
    total_minutes %= 60
    total_hours %= 24

    # Format the output
    local_time = '{:02}:{:02}:{:02}:{:03}'.format(total_hours, total_minutes, total_seconds, milliseconds)
    return local_time


utc_time = input("Enter a time (hh:mm:ss.sTZD):\n")
local_time = convert_time(utc_time)
print("The local time is", local_time)
