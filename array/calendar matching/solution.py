# time = O(c1+ c2)
# space = O(c1+ c2) where c1 and c2 = respective numbers of meetings in calendar1 and calendar 2
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    updatedCalendar1 = updateCalendar(calendar1,dailyBounds1)
    updatedCalendar2 = updateCalendar(calendar2,dailyBounds2)
    mergedCalendar = mergeCalendars(updatedCalendar1,updatedCalendar2)
    flattenedCalendar = flattenCalendar(mergedCalendar)
    return getMatchingAvaibilities(flattenedCalendar,meetingDuration)

def updateCalendar(calendar, dailyBounds):
    updatedCalendar = calendar[:] # copy the original calendar to prevent mutation during maniplication
    updatedCalendar.insert(0, ["0:00",dailyBounds[0]])
    updatedCalendar.append([dailyBounds[1],"23:59"])
    # 1hr >> 60 mins
    # change all the time into minutes
    return list(map(lambda m: [TimeToMinutes(m[0]),TimeToMinutes(m[1])],updatedCalendar))
    # returned time format >> [[0,150],[280,940]]

def mergeCalendars(calendar1, calendar2):
    """ arrange two calendar in a serial order in a new array"""
    merged = []
    i,j = 0,0
    while i< len(calendar1) and j < len(calendar2):
        meeting1, meeting2 = calendar1[i], calendar2[j]
        if meeting1[0] < meeting2[0]:
            merged.append(meeting1)
            i += 1
        else: 
            merged.append(meeting2)
            j += 1
    # one calendar will go out of length first 
    while i < len(calendar1):
        merged.append(calendar1[i])
        i += 1
    while j < len(calendar2):
        merged.append(calendar2[j])
        j += 1
    return merged

    

def flattenCalendar(calendar):
    """flatten the calendar if one meeting starts before the end of another meeting"""
    flattened = [calendar[0][:]] # ??? what is this format [:] = copy the content in that index : stays
    for i in range(1, len(calendar)):
        currentMeeting = calendar[i]
        previousMeeting = flattened[-1] # *****
        currentStart, currentEnd = currentMeeting
        previousStart, previousEnd = previousMeeting
        if previousEnd >= currentStart:
            newPreviousMeeting = [previousStart, max(previousEnd, currentEnd)] # new end will take the longer end
            flattened[-1]= newPreviousMeeting
        else:
            flattened.append(currentMeeting[:]) # append the copy of the curerntMeeting
    return flattened

def getMatchingAvaibilities(calendar, meetingDuration):
    matchingAvailabilites = []
    for i in range(1,len(calendar)):
        start = calendar[i-1][1]
        end = calendar[i][0]
        avaibilityDuration = end-start
        if avaibilityDuration >= meetingDuration:
            matchingAvailabilites.append([start,end])
    return list(map(lambda m:[minutesToTime(m[0]),minutesToTime(m[1])],matchingAvailabilites))

def TimeToMinutes(time):
    """ return minutes"""
    hours, minutes = list(map(int,time.split(":")))
    # list of minutes in integer
    return hours*60 + minutes

def minutesToTime(minutes):
    hours = minutes//60 # divide and round  no round in c++
    mins = minutes%60
    hoursString = str(hours)
    minutesString = "0" + str(mins) if mins < 10 else str(mins)
    return hoursString + ":" + minutesString

calendar1= [
    ["10:00", "10:30"],
    ["10:45", "11:15"],
    ["11:30", "13:00"],
    ["14:15", "16:00"],
    ["16:00", "18:00"]
  ]
dailyBounds1= ["9:30", "20:00"]
calendar2= [
    ["10:00", "11:00"],
    ["12:30", "13:30"],
    ["14:30", "15:00"],
    ["16:00", "17:00"]
  ]
dailyBounds2=["9:00", "18:30"]
meetingDuration= 15
print(calendarMatching(calendar1,dailyBounds1,calendar2,dailyBounds2,meetingDuration))