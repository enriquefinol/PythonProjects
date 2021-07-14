import re

def add_time(start, duration,day=False):

    daysWeekIndex = {"monday":0,"tuesday":1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}
    daysWeekArray = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    am_pm_flips={"AM" : "PM", "PM" : "AM"}

    splitTime = re.split("\s",start)
    dayFormat=splitTime[1]
    hoursMinutesStart = re.split(":",splitTime[0])
    hoursMinutesDuration = re.split(":",duration)

    hoursStart = int(hoursMinutesStart[0])

    hoursDuration = int(hoursMinutesDuration[0])

    totalMinutes =int(hoursMinutesStart[1]) + int(hoursMinutesDuration[1])

    amountDays = hoursDuration // 24

    if (totalMinutes > 60):
        totalMinutes = totalMinutes%60
        hoursStart += 1

    totalHours = hoursStart + hoursDuration
    finalHour = (totalHours%12)

    if(finalHour==0):
        finalHour=12

    if(dayFormat == "PM" and hoursStart + (hoursDuration%12) >= 12):
        amountDays += 1

    numberChanges = totalHours//12
    if(numberChanges %2 == 1):
        dayFormat = am_pm_flips[dayFormat]

    new_time = str(finalHour) + ":" + str(totalMinutes).rjust(2,"0")+ " " + dayFormat

    if(day):
        startDay = daysWeekIndex[day.lower()]
        endDay = daysWeekArray [(startDay + amountDays) %7]
        new_time += ", " + endDay

    if(amountDays ==1):
        new_time += " (next day)"
    elif(amountDays > 1):
        new_time += " (" + str(amountDays) + " days later)"
        
    return new_time
