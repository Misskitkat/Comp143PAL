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