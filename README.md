This question concerns parsing (processing) strings that represent 24-hour clock times expressed as
a Coordinated Universal Time (UTC) with time zone offset.
What do we mean? By way of example, at the time of writing, the time in Cape Town is 15:40:48.
Between 1st January 2017 and 31st December 2017, Cape Town observes South Africa Standard Time
(SAST). SAST is UTC + 2 hours. Expressed as UTC plus time zone offset, the Cape Town time of
15:40:48 is 13:40:48+02.
Write a program called ‘converttime.py’ that will accept a UTC with time zone offset in the
following format:
hh:mm:ss.sTZD
e.g. 19:20:30.45+01
hh = two digits of hour (00 through 23) (am/pm NOT allowed)
mm = two digits of minute (00 through 59)
ss = two digits of second (00 through 59)
s = one or more digits representing a decimal fraction of a second
TZD = time zone designator (+hh or -hh)
The program will print the local time as hours, minutes, seconds and milliseconds. Milliseconds will
be rounded up to 3 decimal places.
