vaction_poll = {}

while True:
    user = input('Enter your name: ')
    place = input('If you could visit one place in the world, where would you go?')

    vaction_poll[user] = place

    repeate = input('Would you like to let another person respond? (yes/ no)')
    if repeate == 'no':
        break

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, place in vaction_poll.items():
    print(f"{name} would like to climb {place}.")