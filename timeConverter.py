from datetime import datetime
from pytz import timezone

class TimeConverter: 
    def __init__(self, datetimeObj, timeZone = None):
        if not datetimeObj.tzinfo:
            try:
                datetimeObj.replace(tzinfo=timezone(timeZone))
            except:
                print("No time zone information could be found")

        self.timeInUTC = self.getTimeInUTC(datetimeObj)
        

    def getTimeInUTC(self, datetimeObj):
        return datetimeObj.astimezone(timezone('UTC'))