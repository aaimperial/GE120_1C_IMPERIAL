import math

def dd_to_dms(degrees):
    d = int(degrees)
    m = int((degrees - d) * 60)
    s = (degrees - d - m / 60) * 3600
    return d, m, s

def print_table(lines):
    print("Line Number\tDistance\tBearing")
    for i, line in enumerate(lines, start=1):
        bearing_dms = dd_to_dms(line['azimuth'])
        print(f"{i}\t\t{line['distance']}\t\t{bearing_dms[0]}°{bearing_dms[1]}'{bearing_dms[2]:.2f}\"")

lines = []
line_number = 1

while True:
    distance = float(input("Enter distance of line (in decimal degrees): "))
    azimuth = float(input("Enter azimuth of line (in decimal degrees): "))
    
    lines.append({'distance': distance, 'azimuth': azimuth})
    
    create_new = input("Do you want to create a new line? (yes/no): ").strip().lower()
    if create_new != 'yes':
        break

print_table(lines)