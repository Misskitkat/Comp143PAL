"""
This file is for chapter 4 and the uses of lists.
How to iterate through a list, different ways to do it?
What is a Tuple and what is the difference between that and a list?

"""

# for element in list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print('1. ')
    print(magician)
print(magicians)
# does the output look like you thought it would for this?
# what the for loop is taking is, each 'magician' is an index in magicians and stored as the magician variable
# we are printing it here but we can do many other things to it than just print it
# the ':' is also very important as it is the syntax to tell python that the code after this with 'tab' characters
# all goes together
# when there are no more indexes in the list to go through, the code breaks out of that loop and goes to the
# code below it.
# make sure you have the correct number of indents so that python knows what you are doing.

# for value in range()
for value in range(1, 5):
    print(value)

# this is going to print 1 2 3 4 on their own lines, it will not reach 5 because range is not
# including the last number.
# when you have a range it includes the first number, and goes up until the last number in the range

# if you want 5 to be printed, up the range by one.
for value in range(1, 6):
    print(value)
# this prints 1 2 3 4 5 and NOT 6

# you can make a list with this
numbers = list(range(1,20))
print(f'Numbers 1-20: {numbers}')  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# this gives you a list of all values from 1-19

# you could make a list of just odd values, you can do
numbers = list(range(1,20,2))
print(f'Odd numbers: {numbers}')  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# you could make a list of just even values, you can do
numbers = list(range(2,21,2))
print(f'Even numbers: {numbers}')  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# you can also manipulate those numbers
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(f'Squares: {squares}')  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# you can also find the min and max of a list of numbers
digits = []
for value in range(1,11):
    digits.append(value)

print((f'Sum: {min(digits)}'))  # 1
print((f'Sum: {max(digits)}'))  # 10
# and the sum
print((f'Sum: {sum(digits)}'))  # 55

# there are also list comprehensions (one line of code for a whole for range list)
squares = [value**2 for value in range(1,11)]
print(f'List comprehension: {squares}')

# you can also work with just part of a list rather than a whole list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(f'These are the players from 1-3: {players[1:4]}')

# you can also just go from the start of the list to a certain amount in the list
print(f'These are the players from 0-3: {players[:4]}')
# this way you only need one number, but it goes from the start to that number.

# or the opposite way you can go from an index to the last element.
print(f'These are the players from 1-(last index): {players[1:]}')

# if you want the last few from a list you can instead do:
print(f'These are the players from -2:(last element): {players[-2:]}')

# COPYING A LIST
# setting a variable equal to another list does not copy over the values of that list,
# it instead is another name for that list.
# if you call both variables you get the same list even if you only append something to one and not the other
# as an example of this:
my_players = players
print(f'Printing my player list: {my_players}')
print(f'Printing the original player list: {players}')

players.append('jordyn')
print(f'Printing my the new player list: {players}')
print(f'Printing my player list: {my_players}')
# here you can see that these lists are the same even if i only appended to one list and not the other.
# they hold the same memory address (the place where the list is stored, and both pull the same list)

# instead how you actually COPY a list is this way:

my_players = players[:]
print(f'Printing my player list: {my_players}')
print(f'Printing the original player list: {players}')
my_players.append('anthony')
print(f'Printing my new player list: {my_players}')
print(f'Printing the original player list: {players}')
# here you can see that anthony was added to my list and not the original players list

# TUPLES:
# tuples are like lists but are immutable, meaning they cannot be changed. Lists are mutable and can be added to,
# and taken away from
# say we wanted a rectangle to stay at specific dimensions and never change

dimensions = (200,50)
print(f'rectangle dimension at 0: {dimensions[0]}')
print(f'rectangle dimension at 1: {dimensions[1]}')
# if can print out those values but if you try to append to dimensions, it throws an error because .append
# is not a method that tuples can use.

# you can overwrite a tuple; that doesn't mean the elements of the tuple can be changed. What you are doing is
# changing what that variable equals.

dimensions = (400,500)
print(f'modified rectangle dimension at 0: {dimensions[0]}')
print(f'modified rectangle dimension at 1: {dimensions[1]}')


