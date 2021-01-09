from collections import defaultdict

class MeetingDatabase:
    def __init__(self):
        self.meetingDir = defaultdict(dict)

    def addMeeting(self, meetingObj, token):
    """Add a meeting to meetingDir
    
    Parameters
    ----------
    meetingObj : the meeting object with all collaborators
    token : the key to the meeting
    
    """
        self.meetingDir[token] = meetingObj


    def removeMeeting(self, token):
    """Remove from a meeting form meetingDir

    Parameters
    ----------
    token : the key to the meeting"""
        self.meetingDir.pop(token, None)