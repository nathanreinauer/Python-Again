import datetime

# Setting up time variables
hourPort = int(datetime.datetime.now().strftime("%H"))
minute = int(datetime.datetime.now().strftime("%M"))
hourNY = hourPort + 3

# Just in case NY time +3 is more than 24
if hourNY >= 24:
    hourNY = hourNY - 24

# Dividing AM and PM for Portland
if hourPort >= 13:
    hourPort = hourPort - 12
    portlandTime = str(hourPort)+':'+str(minute)+' PM'
else:
    portlandTime = str(hourPort)+':'+str(minute)+' AM'

# Dividing AM and PM for New York
if hourNY >= 13:
    hourNY = hourNY - 12
    nyTime = str(hourNY)+':'+str(minute)+' PM'
else:
    nyTime = str(hourNY)+':'+str(minute)+' AM'


# Making sure this works
print portlandTime
print nyTime

