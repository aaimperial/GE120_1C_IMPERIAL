"""
Exercise 1
GE 120
Andrea Imperial
"""
dms = 118.42069

#get degrees part
degree = int(dms)

#get minutes part
minutes_whole = (dms - degree) * 60

#get integer of minutes
minutes_int = int(minutes_whole)

#get seconds
seconds = (minutes_whole - minutes_int) * 60

#put in proper format for submission
print("DMS:" + str(degree) + "-" + str(minutes_int) + "-" + str(round(seconds,2)))



dms = "118-25-14.48"

#get each value for computation
values = dms.split("-")

#get degree integer
degrees = int(values[0])

#get minutes integer
minutes = int(values[1])

#get seconds value
seconds = float(values[2])

#apply necessary computations for minutes and seconds
dd = degrees + (minutes/60) +(seconds/3600)

#put in proper format for submission
print("Value:", round(dd,6))