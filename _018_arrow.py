"""
arrow
"""
import arrow
from dateutil import tz

if __name__ == '__main__':
    now = arrow.Arrow(1995, 6, 8, 13, 30)
    # now = arrow.utcnow()
    print(now.format('YYYY-MM-DD  HH:mm:ss'))
    print(now.datetime)
    print(now.date())
    print(now.time())
    print(now.naive)
    print(now.to("+09:00"))
    print(now.floor('hour'))
    print(now.ceil('hour'))
    print(now.humanize(arrow.utcnow()))  # now.humanize(arrow.utcnow()) 等价
    print(now.utcoffset())
    print(now.timestamp)
    print(now.year)
    print(now.month)
    print(now.day)
    print(now.hour)
    print(now.minute)
    print(now.second)
    print(now.replace(hour=14, minute=33))
    tz = tz.gettz('US/Pacific')
    print(now.to(tz))
    print(now.span('hour'))
    print(now.dst())
