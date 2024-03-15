"""
This is going over the things you can do with lists, chapter 3.
If there is something you are specifically looking for try to search for it. with ctrl/command + f
"""

# this list is directly out of the book in chapter 3
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# printing it to show how the list is printed out, what the syntax is
print(bicycles)  # ['trek', 'cannondale', 'redline', 'specialized']

# how do you access those elements?
# first know that each element is at a specific number, that number starts at 0

print(bicycles[0])  # trek
# if you wanted to get at cannondale that would be 1, redline 2, specialized 3

# the elements of this list are strings so once you access an index you can perform the same
# modifications as the strings
print(bicycles[0].capitalize())  # Trek

# if you didnt know how many elements there were in the list, you can use -1 to get the last one
print(bicycles[-1])  # specialized

# these can also go into fstrings like variables with strings
print(f"Would you like to buy the {bicycles[0].capitalize()}?")  # Would you like to buy the Trek?

# you can also remove and change elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  # ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)  # ['ducati', 'yamaha', 'suzuki']
# you are replacing the value of index 0 to be 'ducati' so the original 'honda' element is replaced

# you can also add to the list instead of replace elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  # ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)  # ['honda', 'yamaha', 'suzuki', 'ducati']
# append adds the element to the end of the list

# you can also insert
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  # ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)  # ['ducati', 'honda', 'yamaha', 'suzuki']
# you can insert an element into a specific index, everything at that index and after is moved down the line by 1.
# as you can see from the output, ducati was put in where honda was and everything was shifted down one

# you can also remove items from the list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  # ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)  # ['yamaha', 'suzuki']
# changing the 0 to 1 or 2 will also change what element will be deleted
# del specifically deletes the element selected and you can never get it back after that line of code

# you can also remove using a different method
# this method allows you to keep the element to be used later on if you need
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  # ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)  # ['yamaha', 'suzuki']
print(popped_motorcycle)  # honda
# pop specifically only pops the index chosen but also saves it to a variable so that you can access it later
print(f"The first motorcycle I owned was a {popped_motorcycle}.")
# this shows how you could use the popped element later on

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  # ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop(2)
print(motorcycles)  # ['honda', 'yamaha']
print(popped_motorcycle)  # suzuki

# you can also just use remove() to get rid of an element
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  # ['honda', 'yamaha', 'suzuki']
motorcycles.remove('yamaha')
print(motorcycles)  # ['honda', 'suzuki']

# you can also sort through a list
alphabet = ['a','b','c','g','i','e','d','h','f']
print(alphabet)  # ['a', 'b', 'c', 'g', 'i', 'e', 'd', 'h', 'f']
alphabet.sort()
print(alphabet)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# it is sorted based on the first letter to the last letter

# or sort if in reverse
alphabet = ['a','b','c','g','i','e','d','h','f']
alphabet.sort(reverse = True)
print(alphabet)  # ['i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
# you can see how it sorts the list but then flips it so that i is first and a is last

# if you want to reverse the order of the list you can do that too
alphabet = ['a','b','c','g','i','e','d','h','f']
alphabet.reverse()
print(alphabet)  # ['f', 'h', 'd', 'e', 'i', 'g', 'c', 'b', 'a']
# the only order to this is the original one is flipped, instead of f being last it is first, and a is last and
# everything else between followed that pattern.

# AS A REMINDER
# INDEX STARTS AT 0 MEANING IF YOU HAVE 3 ELEMENTS YOU CANNOT GET TO THE 3RD INDEX AS THAT DOES NOT EXIST FOR THAT
# LIST. YOU NEED TO INDEX INTO 0,1,2 FOR A LIST OF 3 ELEMENTS (or -1, -2 -3)

