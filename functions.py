import math

# ~~~~~ openFile ~~~~~
## opens a file in read mode
## filename received as a parameter
def openFile(filename):
    try:
        infile = open(filename, "r")

        print("File opened.")

    except:
        print("File not found.")
# ~~~~~
        

# ~~~~~ numbers ~~~~~
## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    return num1 / num2

## takes in two points
## finds the distance between the points
def dist(x1, y1, x2, y2):
    dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
    dist = math.sqrt(dist)

    return dist
# ~~~~~


# ~~~~~ isPalindrome ~~~~~
## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):
    test = temp[::-1]

    if(test == temp):
        return True

    else:
        return False
# ~~~~~


# ~~~~~ divide ~~~~~
## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))

        div = num1 / num2

        print("Your numbers divided is:", div)

    except ZeroDivisionError:
        print("ZeroDivisionError: division by zero")

    except ValueError:
        print("ValueError: invalid literal for int() with base 10")
# ~~~~~


# ~~~~~ sq ~~~~~
## returns the squareroot of a particular number
def sq(num):

    try:
        sqrt = math.sqrt(num)
        return(sqrt)
        
    except ValueError:
        print("ValueError: invalid literal for int() with base 10")


    except:
        print("Value entered must be an integer")
# ~~~~~


# ~~~~~ greetUser ~~~~~
## grabs user's name
## greets them by their entire name
## names should be strings that only accept letters! (A-Z, a-z)
def greetUser(first, middle, last):
    print("Hello!")
    print("Welcome to the program", first, middle, last)
    print("Glad to have you!")
# ~~~~~


# ~~~~~ displayItem ~~~~~
## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    print("Your item at", index, "index is", numbers[index])
# ~~~~~
