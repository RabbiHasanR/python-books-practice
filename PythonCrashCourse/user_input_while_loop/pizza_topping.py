prompt = 'Enter pizza topping:'
prompt += 'Enter quit to exit the program.'

active = True
while active:
    pizza_topping = input(prompt)
    if pizza_topping == 'quit':
        active = False
    else:
        print(pizza_topping)
