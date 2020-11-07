filename = 'programmin_poll.txt'
prompt = "Why do you like programming?:"
prompt += "(for quit enter 'q')"
while True:
    qoute = input(prompt)
    if qoute == 'q':
        break
    with open(filename, 'a') as file_object:
        file_object.write(f"{qoute}\n")