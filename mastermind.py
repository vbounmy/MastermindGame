from random import choice

combination_size = ["", "", "", ""]
# possible_colors = ["🔴", "🟠", "🟡", "🟢", "🔵", "🟣"]
# possible_colors = ["\U+1F534", "\U+1F7E0", "\U+1F7E1", "\U+1F7E2", "\U+1F535", "\U+1F7E3"]
possible_numbers = ["1", "2", "3", "4", "5", "6"]
number_of_attempts = 10
combination = []

def create_combination(combination):
    for _ in combination_size:
        combination += choice(possible_numbers)
    # print(combination)
    return combination

def player_gameplay():
    print("Enter (one by one) 4 numbers among the following list")
    print(possible_numbers)
    player_proposition_in_list = []

    player_proposition = input()
    player_proposition_in_list = list(player_proposition)

    print('Your proposition is ' + str(player_proposition_in_list))
    return player_proposition_in_list

create_combination(combination)
player_gameplay()

