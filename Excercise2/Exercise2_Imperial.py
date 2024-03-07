"""
Exercise 2
GE 120
Andrea Imperial
"""
#CREATE SENTINEL CONTROLLED LOOP
counter = 1

while True:
    print("LINE NO.", counter)
    distance = input("Distance: ")
    azimuth = input("Azimuth: ")

    yn = input("Add new line? ")
    if yn == "YES":
        counter = counter + 1
        continue
    else:
        break

print("-----END-----")
