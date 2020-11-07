guests = ['Piash', 'Borna', 'Tuhin']
print(f'iviting {guests[0]}')
print(f'iviting {guests[1]}')
print(f'iviting {guests[2]}')

print(guests[-1])

guests[0] = 'Rabbi'
print(f'iviting {guests[0]}')
print(f'iviting {guests[1]}')
print(f'iviting {guests[2]}')

guests.insert(0, 'Nayeem')
guests.insert(2, 'Mimmi')
guests.insert(-1, 'Tasmia')
print(guests)

pop_guest_1 = guests.pop()
pop_guest_2 = guests.pop()
pop_guest_3 = guests.pop()
pop_guest_4 = guests.pop()

print(guests)

del guests[0]
del guests[0]
print(guests)