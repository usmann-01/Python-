# this is how to add comments in python.
# comments are notes for youself or callaborators,
# which is ignored by the python compiler.

number = 25
condition = False
floating = 25.76
complex_no = 1+2j
string = "Hello World"
listing = [1,2,3,4,5]
tuple1 = ("hello" , 1 , False)
dictionary = {"name":"Python" , "Version" : "13.7"}
setVar = {1,2,10}
# run the program to know the basic data types 
print(type(number) , type(condition) , type(floating))
print(type(complex_no) , type (string) , type(listing))
print(type(tuple1) , type(dictionary) , type(setVar))

# OPERATORS 

#  Arithmetic Operators : + , - , * , / , % , ** 
#  Assignment Operators : = , += , -= , *= , /= 
#  Comparison Operators : < , > , <= , >= , == , =!
#  Logical Operators    : and , or , not
#  Bitwise Operators    : | , & , ~ (not) , << , >> , ^ (xor)
x = 25 + 35
y = 25 & 35
z = x << 2
print (x,y,z)
print (25 % 6)
# Precedence : Parenthesis , Exponent , Unary , (*  /  %) , (+ -) ,
#              Bitwise (<<  >>  &  ^  |) , Comparisions , Logical
print(x+y*7/10)

