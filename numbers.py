"""
This is a file all about numbers and what operators you can use and what they do to numbers.

"""

print(2 + 3)  # 5
print(9 - 5)  # 4
print(4 * 8)  # 32
print(4 / 2)  # 2.0
print(4 // 2)  # 2
# do you see the difference between one / and two //?
# the / is for float division, a float is any number with a decimal so even if there isn't a decimal, the
# .0 shows that it is a float number and not an integer
# the // is for integer division

print(10 * .009)  # .09
# multiplying an integer by a float makes the product a float value in the end

# what if we wanted to change a float to an integer? Will 3.6 as a float number become 4?
print(int(3.6)) # 3
# python basically just chops off the decimal entirely and keeps everything before the decimal point
# plus this also happens to integer division
print(5 // 2)  # 2
# instead of 2.5 or 3 or 2.0, you get 2

# you can also change an integer to a float
print(float(9))  # 9.0

# you can also change a string containing a number for a float
print(int("7"))

print(9 % 4)  # 1
# this is modulus, this gives you the remainder of an integer division
# 4 goes into 9 twice as 8, 8 taken away from 9 is 1 leaving 1 as the remainder and the answer to 9%4

# how do you think you would be able to do exponent?
print(2 ^ 6)  # 4
# this is a bitwise xor, not something you need to know but I will explain as easily as I can
# in binary 2 = 010 and 6 = 110, xor means only or, so when comparing these two, the only or comes out to
# 100 or 4 YOU DO NOT NEED TO WORRY ABOUT THIS, just know ^ does not mean exponent
# this one means exponent
print(2 ** 6)  # 64

# setting up a variable to do stuff to it
x = 10
print(x)  # 10

# this is an easier way to say x = x + 3
x += 3
print(x)  # 13

x -= 4
print(x)  # 9

# you can apply this to any of the above operators (+, -, *, /, //, **, %, ^, etc)

# if you are going to do multiple operators in one line of code make sure you use PEMDAS
# (Parenthesis, Exponents, Multiplication, Division, Addition, Subtraction)

print(10 - 4 * 8 + 9 // 3)  # -19

print(5 + 4 - 7 + 3)  # 5

# you can also compare numbers and get a boolean (true or false) value in return
print(2 > 10)  # False
print(8 > 5)  # True

