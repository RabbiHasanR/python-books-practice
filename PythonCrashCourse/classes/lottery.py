from random import choice

def randomly_selected_lottery_numbers(numbers):
    """Return randomly selected lottery numbers"""
    num_0 = choice(numbers)
    num_1 = choice(numbers)
    num_2 = choice(numbers)
    num_3 = choice(numbers)

    return num_0, num_1, num_2, num_3

lottery_numbers = [10, 7, 8, 9, 1, 2 , 5, 4, 6, 3, 'r', 'a', 'b', 'i']
random_lottery_numbers = randomly_selected_lottery_numbers(lottery_numbers)
print(f"{random_lottery_numbers} this numbers matche is win lottery")

def check_ticket_number_lottery(my_ticket):
    while True:
        random_lottery_numbers = randomly_selected_lottery_numbers(lottery_numbers)
        print(f"Win Lottery numbers: {random_lottery_numbers}")

        if my_ticket == random_lottery_numbers:
            print("You win the lottery!")
            break

my_ticket = (7, 3, 'i', 6)
check_ticket_number_lottery(my_ticket)