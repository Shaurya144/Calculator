# this python calculator does symple arrithmatic calculations 
# how i plan on doing this is by creating three functions Add, Subtract, Multiply, Divide and Options

def addition():
    while True:
        try:
            number1 = int(input("number 1: "))
            number2 = int(input("number 2: "))
            answer = number1 + number2

            return answer
        
        except ValueError:
            print("Enter an integer")



def subtraction():
    while True:
        try:
            number1 = int(input("number 1: "))
            number2 = int(input("number 2: "))
            answer = number1 - number2
            
            return answer

        except ValueError:
            print("Enter an integer")



def multiplacation():
    while True:
        try:
            number1 = int(input("number 1: "))
            number2 = int(input("number 2: "))
            answer = number1 * number2
            
            return answer

        except ValueError:
            print("Enter an integer")



def division():
    while True:
        try:
            number1 = int(input("number 1: "))
            number2 = int(input("number 2: "))
            answer = number1 / number2
            
            return answer
        
        except ZeroDivisionError:
            print("You can't divide by zero!")

        except ValueError:
            print("Enter an integer")



def Options():
    while True:
        choice = input("Please type Add, Subtract, Multipl or Divide to select the option. Type QUIT to exit. ")
        if choice == "QUIT":
            break
        elif choice == "ADD" or "add" or "Add" or "Addition":
            answer = addition()
            print("The Answer is .... ",answer)

        elif choice == "SUBTRACT" or "subtract" or "Subtract" or "Subtraction":
            answer = subtraction()
            print("The Answer is .... ",answer)

        elif choice == "Multiply" or "multiply" or "Multipy" or "multiplacation":
            answer = multiplacation()
            print("The Answer is .... ",answer)

        elif choice == "DIVIDE" or "divide" or "Divide" or "Division":
            answer = division()
            print("The Answer is .... ",answer)
        else:
            print("Please type Add, Subtract, Multipl or Divide to select the option.")

Options()
