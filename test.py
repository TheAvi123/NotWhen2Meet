calendar_list_entry = service.calendarList().get(calendarId='calendarId').execute()

print(calendar_list_entry['summary'])