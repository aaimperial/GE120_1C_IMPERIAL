'''

LEVELLING SURVEY COMPUTATIONS
Andrea Imperial
Computations for direct levelling

'''

print("Levelling Survey Computations")      # title of program
print("Andrea Imperial")                    # name of maker
print("Computations for direct levelling")  # description of program

'''

levelling_table - list of tuples, appending measurements and derived values
    levelling_table
        tuple_1 = BS values
        tuple_2 = FS values
        tuple_3 = HOI values
        tuple_4 = Elev values

total_distance - float value, stores sum of all distances between turning points
    total_distance = float(X)
        X = summation of d_TP

tp_counter - integer value, stores number of turning points between benchmarks
    tp_counter = int(Y)
        Y = number of TPs

'''

def floatInput():
    # Converts input to float
    prompt = float(input("Elevation: "))
    return prompt

tp_counter = 1
lines = []

Elev = input("Initial Elevation of BM0? ")


while True:
    print("TP", tp_counter)
    BS = input("Backsight(in m): ")
    FS = input("Foresight(in m): ")
    d_TP = input("Distance between turning points: ")
    # input of values

    HOI = Elev + BS
    # Height of Instrument = Running Elevation + Backsight Measurement

    RunElev = HOI - FS
    # Elevation = Height of Instrument - Foresight Measurement


    levelling_table = (BS, FS, d_TP, HOI)   #saving all needed values
    levelling_table.append(levelling_table)

    yn = input("Create new measurement? ")
    if yn.lower() == "yes" or yn.lower() == "y":
        tp_counter = tp_counter + 1
        continue
    else:
        break

def print_as_table(*lines):
    print('{: ^10} {: ^10} {: ^10}'.format("Sta.", "B.S", "H.I", "F.S", "Elev"))
    for line in lines:
        print('{: ^10} {: ^10} {: ^10}'.format(line[0], line[1], line[2]))

    print_as_table(tp_counter, BS, HOI, FS, RunElev)