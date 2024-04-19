def example(name):
    print ("Hi")
    print (name)

def namesfunction(first):
    print("Hi")
    print(first,"Edwards")

def subtract(a,b):
    return (a-b)

def compare(a,b,opposite=0):
    if (a > b and opposite == 0):
        print(a,"is greater than",b)
    elif (a == b):
        print(a,"is equal to",b)
    elif (a>b and opposite == 1):
        print(b,"is not greater than",a)
    else:
        print(a,"is not greater than",b)
        
    

example("Vikram")
namesfunction("John")
namesfunction("Frank")
namesfunction("Greg")
x = subtract(12,5)
print(x)
compare(35,12)
print("Enter numbers to compare")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
compare(num1,num2,1)



