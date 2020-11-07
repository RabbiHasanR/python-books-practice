prompt = "Enter your age:"
prompt += "Enter 0 to exit program."

while True:
    age = input(prompt)
    age = int(age)
    if age == 0:
        break

    if age <= 3:
        price = 0
    elif age <= 12 :
        price = 10
    elif age > 12:
        price = 15
    
    print(f"Movie ticket price for you ${price}")
    
    
