#KEYWORD ARGUMENT
#kwargs is an arbitary argument and it is defined with ** before the prameter in fun defenition

def my_function(**product):
    print("the products that are recived today is" ,product["p2"])

my_function(p1="chilly",p2="maggie",p3="flour")