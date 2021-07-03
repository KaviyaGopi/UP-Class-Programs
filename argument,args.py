#ARBITARY ARGUMENTS ,Args
#if u dont know how many arguments to be passed inside ur function,you can add a * before the parameter inside the function call 
#for example 
def my_function(*marks):
    print(f"the highest marks got  by the child is {marks[1]}")

my_function(100,96,101,46)