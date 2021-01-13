# Handle the exception thrown by the code below by using try and except blocks.
def problem1():
    try:
        for i in [2, 'b', 'c']:
            print(i ** 2)
    except TypeError:
        print("Wrong type of input")


# Handle the exception thrown by the code below by using try and except blocks.
# Then use a finally block to print 'All Done.'
def problem2():
    x = 5
    y = 0
    try:
        z = x / y
    except ZeroDivisionError:
        print("Can't divide by 0")
    finally:
        print("All Done")

    pass


# Write a function that asks for an integer and prints the square of it.
# Use a while loop with a try, except, else block to account for incorrect inputs.
def ask():
    while True:
        try:
            num = int(input("Input an integer: "))
        except ValueError:
            print("An error occurred! Please try again!")
        else:
            break
    print("Thank you, your number squared is: " + str(num**2))


if __name__ == '__main__':
    problem1()
    problem2()
    ask()

