"""
This is the file that will go over what booleans are and how you can use them. As well as
some of the logic that comes up with booleans and comparisons.

"""

print(4 < 5)  # True
# this prints True as 4 is less than 5

print(5 < 4)  # False
# this prints False as 5 is not less than 4

# a boolean can only be true or false:
# the datatype is bool

print(0 <= 0)  # True
# you can also add an equals sign next to < or > making it greater/less than or equal to.

print(9 == 9)  # True
# you can also compare statements with the double ==, one = sets a variable to a value, == compares two values

age = 10
age += 8
print(18 == age)  # True
# you can also use variables
print(17 != age)  # True

# what can we do when comparing strings?
car = 'audi'
print(f"car is an audi: {car == 'audi'}")  # True

print(f"car is an AUDI: {car == 'AUDI'}")  # False
# you can see here that the case of the letters matters, a != A

# there are also logical connectives to try out as well;
# and, not, or

# what do you think this does?
print((3 < 4) and (9 > 4))  # True
# what about this?
print((3 < 4) and (9 < 4))  # False
# or this?
print((3 > 4) and (9 > 4))  # False
# or this?
print((3 > 4) and (9 < 4))  # False

# what happens when you use and?
# and is only true when both expressions being compared are true.
# if one is false, the whole thing is false, if both are false, it is also false.
# sometimes you only want something when both options are true.
# say you liked someone, you say you will go on a date with them if they met your preferences, all of those
# must be true for the date to happen.

# we have and, what about or?

# what happens with this?
print((3 < 4) or (9 > 4))  # True
# that looks similar to before right? what about this
print((3 < 4) or (9 < 4))  # True
# or this?
print((3 > 4) or (9 > 4))  # True
# or this?
print((3 > 4) and (9 < 4))  # False
# FINALLY, got a False
# or is true when one or both/all are True, almost the opposite of and.

# now what about not?
print(True)  # True
print(not(True))  # False
print(not(False))  # True

# here you can see that it changes something that is true, to false, and false to true, it flips it.
# almost like multiplying a negative by a negative flips to a positive and a positive times a negative
# becomes a negative.

# you can also check to see if items are in a list for true or false results:
toppings = ['mushrooms', 'onions', 'pineapple']
print(f"is there mushrooms? {'mushrooms' in toppings}")
print(f"is there pepperoni? {'pepperoni' in toppings}")
