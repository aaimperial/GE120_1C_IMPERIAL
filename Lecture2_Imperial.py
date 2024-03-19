# dfnlknwnnwn
print("Wazzup")
print(int("56"))
print(type("STRING"))
print(type(float(54)))
print(type(3.14159265358))
print(type(1+4j))

x = 2
y = 13

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x ** y)
print(x % y)
print(abs(y))
print(float(y))
print(complex(y))
print(divmod(y,x))

dog = ["golden retriever", "husky", "aspin",]
print(dog)

#========================================================
# DataType Output: str 
x = "Hello World"

# DataType Output: int 
x = 50

# DataType Output: float 
x = 60.5

# DataType Output: complex 
x = 3j

# DataType Output: list 
x = ["geeks", "for", "geeks"] 

# DataType Output: tuple 
x = ("geeks", "for", "geeks") 

# DataType Output: range 
x = range(10) 

# DataType Output: dict 
x = {"name": "Suraj", "age": 24} 

# DataType Output: set 
x = {"geeks", "for", "geeks"} 

# DataType Output: frozenset 
x = frozenset({"geeks", "for", "geeks"}) 

# DataType Output: bool 
x = True

# DataType Output: bytes 
x = b"Geeks"

# DataType Output: bytearray 
x = bytearray(4) 

# DataType Output: memoryview 
x = memoryview(bytes(6)) 

# DataType Output: NoneType 
x = None


#=====================================================
# Examples of Relational Operators 
a = 13
b = 33

# a > b is False 
print(a > b) 

# a < b is True 
print(a < b) 

# a == b is False 
print(a == b) 

# a != b is True 
print(a != b) 

# a >= b is False 
print(a >= b) 

# a <= b is True 
print(a <= b) 

#=======================================================

# Examples of Logical Operator 
a = True
b = False

# Print a and b is False 
print(a and b) 

# Print a or b is True 
print(a or b) 

# Print not a is False 
print(not a) 

#========================================================

# Creating a String 
String1 = "GeeksForGeeks"
print("Initial String: ") 
print(String1) 

# Printing 3rd character 
print("\nSlicing characters from 3-12: ") 
print(String1[3]) 

# Printing characters between 
# 3rd and 2nd last character 
print("\nSlicing characters between " +
	"3rd and 2nd last character: ") 
print(String1[3:-2]) 

# Initial String: 
# GeeksForGeeks
# Slicing characters from 3-12: 
# k
# Slicing characters between 3rd and 2nd last character: 
# ksForGee

#========================================================

# Interpreter
# Compiler
# Translates program one statement at a time.
# Scans the entire program and translates it as a
# whole into machine code.
# It takes a less amount of time to analyze the
# It takes a large amount of time to analyze the
# source code but the overall execution time is
# source code but the overall execution time is
# slower.
# completely faster.
# No intermediate object code is generated,
# Generated intermediate object code which
# hence are memory efficient.
# further requires linking, hence requires more
# memory.
# Continues translating the program until the
# It generates the error message only after
# first error is met, in which case it stops. Hence,
# scanning the whole program. Hence,
# debugging is easy.
# debugging is comparatively hard.
# Programming languages like Python,
# Programming languages like C, C++ use
# JavaScript, Ruby use interpreters.
# compilers.

