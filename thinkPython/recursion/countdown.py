def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

countdown(6)

def print_string(message, n):
    if n <= 0:
        return
    else:
        print(message)
        print_string(message, n-1)

print_string('Rabbi', 5)