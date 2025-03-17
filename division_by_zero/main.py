def number_division():
    number_1 = input('Insert the first number: ')
    number_1 = float(number_1)
    number_2 = input('Insert the second number: ')
    number_2 = float(number_2)

    if number_2 == 0:
        print("Error: Division by zero is not allowed.")
        return
    
    division = number_1 / number_2
    
    print(f"{number_1} divided by {number_2} is {division}")

number_division()
