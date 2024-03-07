"""
Exercise 2
GE 120
Andrea Imperial
"""
#CREATE SENTINEL CONTROLLED LOOP
counter = 1
lines = []

while True:
    print("LINE NO.", counter)
    distance = input("Distance: ")
    azimuth = float(input("Azimuth from the South: "))%360

    if "-" in azimuth: #in DMS
        degree, minutes, seconds 
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
    elif azimuth = 0
        bearing = "DUE SOUTH"
    elif azimuth = 90
        bearing = "DUE WEST"
    elif azimuth = 180
        bearing = "DUE NORTH"
    elif azimuth = 270
        bearing = "DUE EAST"
    elif azimuth = 360
        bearing = "DUE SOUTH"

    line = (counter, distance, azimuth) #create tuple of the line
    lines.append(line)

    yn = input("Add new line? ")
    if yn.lower() == "yes" or yn.lower() == "y":
        counter = counter + 1
        continue
    else:
        break

print("\n\LINES")

for line in lines:
    print('{: ^} {} {}'.format(line{0}, line{1},line))

    print("-----END-----")