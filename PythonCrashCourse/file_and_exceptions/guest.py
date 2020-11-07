filename = 'guest.txt'
prompt = "Enter guest name:"
prompt += "(for quit enter 'q')"
while True:
    guest_name = input(prompt)
    if guest_name == 'q':
        break
    print(f"Hello, {guest_name}")
    with open(filename, 'a') as file_object:
        file_object.write(f"{guest_name}\n")