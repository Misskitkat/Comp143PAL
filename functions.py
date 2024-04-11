def hello_world():
    print("hello world")
    print("good-bye")

def hello_function():
    i = 0
    while (i!=10):
        print("hello")
        i+=1

def input_function():
    input_value = input("Enter your name (or Q to quit): ")
    if(input_value != "Q"):
        print(f'Nice to meet you, {input_value}')
        hello_world()

def add_num(num1,num2):
    print(num1+num2)

add_num(5,7)

