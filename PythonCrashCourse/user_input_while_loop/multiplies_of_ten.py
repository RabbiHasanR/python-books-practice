number = input("Enter number for check number is multiplies of 10 or not: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} multiplies by 10.")
else:
    print(f"{number} not multiplies by 10.")