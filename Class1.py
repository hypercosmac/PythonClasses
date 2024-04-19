from random import randint

#Python Calculator code

operation = input("Enter Calculator Operation (Choose from + or - or * or / or ^): ")
#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))

if operation == "+":
    #print("The answer is: ",num1+num2)
    print(randint(1,3)+randint(1,3))

elif operation == "-":
    print("The answer is: ",num1-num2)

elif operation == "*":
    print("The answer is: ",num1*num2)

elif operation == "/":
    print("The answer is: ",num1/num2)

elif operation == "^":
    print("The answer is: ",num1**num2)

else:
    print("Invalid operation")
