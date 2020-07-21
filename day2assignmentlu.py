# diffrent way to declere varible or check data type
a = 10  
b10 = 20.23  
_c = [30,20] 
print(type("3.0"))

# And operatore
mark1 = 65
mark2 = 41
if mark1 > 40 and mark2 > 40:
    print("Result: Pass")
else:
    print("Result: Fail")

# Or operator
mark1 = 39
mark2 = 35
if mark1 > 40 or mark2 > 40:
    print("Result: Pass")
else:
    print("Result: Fail")

#  Not operator
if not(True):
    print("condition is true")
else:
    print("condition is false")

# is operator
a = 50
b = 60.0
if type(a) is type(b):
    print("A and B are of similar object type")
else:
    print("A and B are of different object type")


# in operator
lst = [10,50,60,45,1,2,-2]
sv = 500
if sv in lst:
    print("Search value is in the list")
else:
    print("Search value is not in the list")

# bitwise operator
a = 50
b = ~a
print(a)

# multipleassignment
# Multiple Assignment
# a, b,c,d = 50,60,70,80
# print(a,b,c,d)

# Swap variable values
# x,y = 100,200
# print(x,y)

# x , y = y , x

#  print(x,y)

a , b = "India",10
print(a,b)

