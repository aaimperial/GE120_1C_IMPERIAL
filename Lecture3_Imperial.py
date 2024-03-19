# # Lecture 3 Notes

# listahan = ["red", "yellow", "green", "blue"]
# print(listahan)

# # to get green (position)
# print(listahan[2])

# # to get a subset of the list, red and yellow
# print(listahan[0:2])

# # 

# # start from index 




# # #gets first item, last item, then those in between
# # print

# # Addition of lists
# print(listahan[0:2]+listahan[2:4])
# print


# listahan[0] = [white , gray, black]

# # TUPLES
# tuple_1 = ("white", "gray", "black")
# print(tuple_1)

# # tuples are immutable
# tuple_1[0] = "stone"

# # NESTED LISTS
# list_1 = [ ["apple", "banana", "grape"] , ["ice cream", "gelato", "shake"] ]

# tuple_2 = [ ("12.5432", "23.6543", "34.7654")]
# print(tuple_2[2][0])

# # DICTIONARIES
# dog = {
#     "name": "Ghost"
#     "age": 9
#     "color": "white with black spots"
#     "favorite food": "hotdog"
#     1.113:45    #pwede si number as key (float or int)
#     }

# print(dog[1.113])
# print(dog.values())
# print(dog.keys())
# print(dog('name'))




# # CONTROL STRUCTURES
# grade = 59 ; favorite = True

# if grade >= 92:
#     print("YAHOO")

# elif grade >= 60:
#     print("NICE")

# elif grade <60 and favorite:
#     print("pasangina")

# else: print("SAD")

# #LOOPS: BREAK, CONTINUE, AND PASS
# numbers = range(50,100)
# for number in range(10):
#     print(number)   #kasama si 5
#     if number == 5:
#         break
#     print(number)   #di na kasama si 5

# for number in range(10):
#     if number == 5:
#         print(number)
#         continue    #5 lang ipiprint

# for number in range(10):
#     if number == 5:
#         pass
#         print(number)   #walang mapiprint after ng pass

# while rec < 5000:
#     rec = input("enter REC:")

# print("PASOK NA REC")
# print("-----END-----")

# rec = 0
# while rec <= 5000:
#     rec =int(input("enter REC: "))
#     kulang = 5000 - rec
#     print("kulang ka ng REC na", kulang)

# print("PASOK NA REC")
# print("-----END-----")

# rec = 0
# while rec <= 5000:
#     rec =int(input("enter REC: "))
#     kulang = 5000 - rec
#     if rec >= 4500:
#         print("onti na kulang, kaya mo yan")
#     print("kulang ka ng REC na", kulang)

# print("PASOK NA REC")
# print("-----END-----")

# rec = 0
# while rec <= 5000:
#     rec =int(input("enter REC: "))
#     kulang = 5000 - rec
#     if rec >= 4500:
#         continue
#         print("onti na kulang, kaya mo yan")
#     print("kulang ka ng REC na", kulang)

# print("PASOK NA REC")
# print("-----END-----")

# rec = 0
# while rec <= 5000:
#     rec =int(input("enter REC: "))
#     kulang = 5000 - rec
#     if rec >= 4500:
#         pass
#         print("onti na kulang, kaya mo yan")
#     print("kulang ka ng REC na", kulang)

# print("PASOK NA REC")
# print("-----END-----")


intro = input('Enter intro: ')
print(intro)