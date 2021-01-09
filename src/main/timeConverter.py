from datetime import datetime
from pytz import timezone

TZ_UNIVERSAL = "UMT"

"""Class to handle our timezone conversions
Flow: we start with a datetime object and convert it to UMT timezone for storage
then we can call convertTimeZone(tzToConvert) to retrieve a converted time of our choice"""
class TimeConverter: 
    def __init__(self, datetimeObj, tz = None):
        if not datetimeObj.tzinfo:
            try:
                datetimeObj.replace(tzinfo=timezone(tz))
            except:
                print("No time zone information could be found")

        self.timeInUTC = datetimeObj.astimezone(TZ_UNIVERSAL)
        
    def getConvertedTimeZone(self, tzToConvert):
        return self.timeInUTC.astimezone(timezone(tzToConvert))