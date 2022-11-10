def additon(numbers):
    return sum(numbers)


def substract(numbers):
    result = numbers[0]
    for x in numbers:
        if x != numbers[0]:
            result -= x
        else:
            continue
    return result


def multiply(numbers):
    result = 1
    for x in numbers:
        result *= x
    return result


def division(numbers):
    result = numbers[0]
    for x in numbers:
        if x != numbers[0]:
            result /= x
        else:
            continue
    return result


def evenOrodd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def Switch(choice):
    choice = int(choice)
    counter = int(0)
    if choice == 1:
        numOfoper = int(input("How many numbers want: "))
        numbers = list()
        while counter < numOfoper:
            num = int(input("Enter the number: "))
            numbers.append(num)
            counter += 1
        counter = 0
        print(additon(numbers))
    elif choice == 2:
        numOfoper = int(input("How many numbers want: "))
        numbers = list()
        while counter < numOfoper:
            num = int(input("Enter the number: "))
            numbers.append(num)
            counter += 1
            counter = 0
            print(substract(numbers))
    elif choice == 3:
        numOfoper = int(input("How many numbers want: "))
        numbers = list()
        while counter < numOfoper:
            num = int(input("Enter the number: "))
            numbers.append(num)
            counter += 1
        counter = 0
        print(multiply(numbers))
    elif choice == 4:
        numOfoper = int(input("How many numbers want: "))
        numbers = list()
        while counter < numOfoper:
            num = int(input("Enter the number: "))
            numbers.append(num)
            counter += 1
        counter = 0
        print(division(numbers))
    elif choice == 5:
        num = int(input("Enter the number: "))
        print(evenOrodd(num))
    elif choice == 6:
        num = int(input("Enter the number: "))
        print(factorial(num))
    else:
        print("Enter Invalid Number")

conExit = 1
while (conExit != 0):
    print("Welcome to Our Calculator")
    print(" (1) Addition (2) Substration (3) Multiplication (4) Division  (5) EvenOrOdd (6) Factorial")
    choice = input("Enter your choice: ")
    Switch(choice)
    conExit = int(input("Press (1) to Continue or (0) to Exit: "))

print("Good Bye")
