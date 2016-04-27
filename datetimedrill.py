import datetime

# Setting up time variables
hourPort = int(datetime.datetime.now().strftime("%H"))
hourNY = hourPort + 3
hourLond = hourPort + 8
minute = int(datetime.datetime.now().strftime("%M"))


# Just in case NY time +3 is more than 24
if hourNY >= 24:
    hourNY = hourNY - 24

if hourLond >= 24:
    hourLond = hourLond - 24

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

# Dividing AM and PM for London
if hourLond >= 13:
    hourLond = hourLond - 12
    londonTime = str(hourLond)+':'+str(minute)+' PM'
else:
    londonTime = str(hourLond)+':'+str(minute)+' AM'



if portlandTime 





# Making sure this works
print portlandTime
print nyTime
print londonTime



