"""
for now this includes an example similar to one of the homework questions that we went over in class.
it is not exact but this is also a way to show what while loops can do.
"""


i = 1
while(i < 25):
    print(i)
    if(i%3 == 0 or i%4 == 0):
        print(i)
    i+=1


current_number = 0

while current_number < 10:
    current_number += 1
    if (current_number % 2 == 0):
        continue

        print(current_number)

# this shows that only the odd numbers will be printed, and the print statement highlighted because it will never
# print and python is trying to give you that heads up.

x=1
while x <= 5:
    print(x)
    x += 1
# if you do forget to put the += there will be an infinite loop because x will never not be 1 without += 1

pets = ['dog', 'cat', 'bunny', 'dog', 'goldfish', 'cat', 'rabbit']
print(pets)
while 'cat' in pets:
        pets.remove('cat')
print(pets)
# this shows how you can remove elements in a list by what element it is and while there is some left in the list.

