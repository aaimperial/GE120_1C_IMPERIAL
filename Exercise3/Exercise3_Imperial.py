"""
Exercise 2
GE 120
Andrea Imperial
"""
from math import cos, sin, radians, sqrt

def getLatitude(distance, azimuth):
    '''
    Compute for'''

    latitude = -distance * cos(radians(azimuth))

    return latitude


    



def getDeparture(distance, azimuth):
    '''
    Compute for'''

    departure = -distance * sin(radians(azimuth))

    return departure

lat = getLatitude(12,160)
dep = getDeparture(12,160)
print(dep)





def azimuthtoBearing(azimuth):
    '''
    Compute for the DMS bearing of a given angle
    Input'''

    azimuth
    if "-" in : #in DMS
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees) + (int(minutes)/60) + (float(seconds)/3600))%360
        #converts DD to DMS
    else:
        azimuth = float(azimuth%360)

    if azimuth > 0 and azimuth < 90:
        bearing = 'S {:^10} W'.format(azimuth)
    elif azimuth > 90 and azimuth < 180:
        bearing = 'N {:^10} W'.format(180 - azimuth)
    elif azimuth > 180 and azimuth < 270:
        bearing = 'N {:^10} E'.format(azimuth - 180)
    elif azimuth < 360:
        bearing = 'S {:^10} E'.format(360 - azimuth)
    elif azimuth == 0:
        bearing = "DUE SOUTH"
    elif azimuth == 90:
        bearing = "DUE WEST"
    elif azimuth == 180:
        bearing = "DUE NORTH"
    elif azimuth == 270:
        bearing = "DUE EAST"
    elif azimuth == 360:
        bearing = "DUE SOUTH"

    return bearing

lat = getLatitude(12,160)
dep = getDeparture(12,160)
print(dep)

bearing = azimuthtoBearing()



counter = 1
lines = []

while True:
    print("LINE NO.", counter)
    distance = input("Distance: ")
    azimuth = float(input("Azimuth from the South: "))%360
    #input of values

    if "-" in azimuth: #in DMS
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees) + (int(minutes)/60) + (float(seconds)/3600))%360
        #convert DD to DMS
    else:
        azimuth = float(azimuth%360)

    if azimuth > 0 and azimuth < 90:
        bearing = 'S {:^10} W'.format(azimuth)
    elif azimuth > 90 and azimuth < 180:
        bearing = 'N {:^10} W'.format(180 - azimuth)
    elif azimuth > 180 and azimuth < 270:
        bearing = 'N {:^10} E'.format(azimuth - 180)
    elif azimuth < 360:
        bearing = 'S {:^10} E'.format(360 - azimuth)
    elif azimuth == 0:
        bearing = "DUE SOUTH"
    elif azimuth == 90:
        bearing = "DUE WEST"
    elif azimuth == 180:
        bearing = "DUE NORTH"
    elif azimuth == 270:
        bearing = "DUE EAST"
    elif azimuth == 360:
        bearing = "DUE SOUTH"

    bearing``



    line = (counter, distance, azimuth) #create tuple of the line
    lines.append(line)

    yn = input("Add a new line? ")
    if yn.lower() == "yes" or yn.lower() == "y":
        counter = counter + 1
        continue
    else:
        break

print("\n\nMGALINES")

for line in lines:
    print('{} {} {}'.format(line[0], line[1],line[2]))

    print("-----END-----")