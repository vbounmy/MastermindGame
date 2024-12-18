from random import choice

# possible_colors = ["🔴", "🟠", "🟡", "🟢", "🔵", "🟣"]
# possible_colors = ["\U+1F534", "\U+1F7E0", "\U+1F7E1", "\U+1F7E2", "\U+1F535", "\U+1F7E3"]

def create_combination(possible_numbers, combination_size):
    combination = []
    for _ in combination_size:
        combination += choice(possible_numbers)
    print("answer" + str(combination))
    return combination

def player_gameplay(possible_numbers, combination_size):
    print("Enter 4 numbers (w/o space) among the following list.")
    print(str(possible_numbers) + " :")

    player_proposition = input()
    player_proposition_in_list = list(player_proposition)
    valid_proposition = True

    for number in player_proposition_in_list:
        if number not in possible_numbers:
            valid_proposition = False

    if len(player_proposition_in_list) != len(combination_size):
        print("Number of entries is incorrect. Please re-enter 4 numbers.")
    elif valid_proposition == False:
        print("You entered an invalid number. Please choose among the possible numbers.")
    else:
        print('Your proposition is ' + str(player_proposition_in_list))

    return player_proposition_in_list

def verification(player_proposition_in_list, combination):
    print("Hints caption : x: incorrect answer, -: right number but wrong position, o: right answer")
    hints = []
    for index, number in enumerate(player_proposition_in_list):
        if number not in combination:
            hints.append("x")
        elif index != combination.index(number):
            hints.append("-")
        else:
            hints.append("o")
    print("Hints : " + str(hints))
    return hints

combination_size = ["", "", "", ""]
possible_numbers = ["1", "2", "3", "4", "5", "6"]
number_of_attempts = 10

combination = create_combination(possible_numbers, combination_size)
player_proposition_in_list = player_gameplay(possible_numbers, combination_size)
verification(player_proposition_in_list, combination)

