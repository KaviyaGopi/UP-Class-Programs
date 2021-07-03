def add(num1,num2):
    return(num1+num2)
def sub(num1,num2):
    return(num1-num2)
def multiply(num1,num2):
    return(num1*num2)
def divide(num1,num2):
    return(num1/num2)
        

print("CALCULATOR")
print("give 1 for addition,2 for subtraction,3 for mutiplication,4 for division")
choice=int(input("enter ur choice"))
num1=float(input("enter ur first no"))
num2=float(input("enter ur second number"))
if choice==1:
    print(f"the addition of first number and second number is{add(num1,num2)}")
if choice==2:
    print(f"the subtraction of first number and second number is{sub(num1,num2)}")
if choice==3:
    print(f"the multiplication of first number and second number is{multiply(num1,num2)}")
if choice==4:
    print(f"the division of first number and second number is{divide(num1,num2)}")