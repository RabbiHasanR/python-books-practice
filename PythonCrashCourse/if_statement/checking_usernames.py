current_users = ['Rabbi', 'Piash', 'Tuhin', 'Alam', 'Admin']
new_users = ['Shaily', 'Sarmin', 'Pushpo', 'Sumona', 'Tuly', 'Rabbi', 'Piash']

for new_user in new_users:
    if new_user in current_users:
        print(f'{new_user} will need to enter a new username.')
    else:
        print(f'{new_user} is available.')
