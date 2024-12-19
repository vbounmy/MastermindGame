from random import choice
from ansi_escape_codes import *

# possible_colors = ["🔴", "🟠", "🟡", "🟢", "🔵", "🟣"]
# possible_colors = ["\U+1F534", "\U+1F7E0", "\U+1F7E1", "\U+1F7E2", "\U+1F535", "\U+1F7E3"]

def create_combination(possible_numbers, combination_size):
    combination = []
    for _ in combination_size:
        combination += choice(possible_numbers)
    # print("secret combination :" + str(combination))
    return combination

def player_gameplay(possible_numbers, combination_size):
    print("Enter 4 numbers (w/o space) among the following list." + "\n" + str(possible_numbers) + " :")

    valid_proposition = False

    while valid_proposition == False:
        player_proposition = input()
        player_proposition_in_list = list(player_proposition)

        if len(player_proposition_in_list) != len(combination_size):
            print("Number of entries is incorrect. Please re-enter 4 numbers.")
        elif any(number not in possible_numbers for number in player_proposition_in_list):
            print("You entered an invalid number. Please choose among the possible numbers.")
        else:
            valid_proposition = True
            print("\n" + 'Your proposition : ' + "\t" + BOLD + str(player_proposition_in_list) + END)

    return player_proposition_in_list

def verification(player_proposition_in_list, combination):
    hints = []
    temp_combination = combination.copy()

    for index, number in enumerate(player_proposition_in_list):
        if number == temp_combination[index]:
            hints.append(BOLD + GREEN + "o" + END)
            temp_combination[index] = None
        else:
            hints.append(None)

    for index, number in enumerate(player_proposition_in_list):
        if hints[index] == None:
            if number in temp_combination:
                hints[index] = BOLD + YELLOW + "-" + END
                temp_combination[temp_combination.index(number)] = None
            else:
                hints[index] = BOLD + RED + "x" + END

    print("Hints : " + "\t"*2 + "[" + ', '.join(hints) + "]")

    return hints

def create_game():
    max_number_of_attempts = 10*[""]
    number_of_attempts = 0
    game_won = False

    combination = create_combination(possible_numbers, combination_size)

    print(BOLD + BLUE + "\n" + "MASTERMIND GAME" + END)
    print(ITALIC + "Try to find the secret combination in 10 attempts." + "\n"*2 + "Hints will be given at the end of each round :" + "\n" + "x : incorrect answer, - : right number but wrong position, o : right answer" + END + "\n")

    for _ in max_number_of_attempts:
        number_of_attempts += 1
        print("-"*45)
        print(BOLD + "Number of attempts : " + str(number_of_attempts) + "/10" + END)
        player_proposition_in_list = player_gameplay(possible_numbers, combination_size)
        hints = verification(player_proposition_in_list, combination)

        if hints == [BOLD + GREEN + "o" + END, BOLD + GREEN + "o" + END, BOLD + GREEN + "o" + END, BOLD + GREEN + "o" + END]:
            game_won = True
            print(BOLD + GREEN + "\n" + "Victory." + "\n" + "You found the secret combination, GG !" + END)
            break
        elif game_won == False:
            if number_of_attempts < 10:
                print("Wrong combination, please retry." + "\n")
            else:
                print(BOLD + RED + "\n" + "Defeat." + "\n" + "The secret combination was " + str(combination) + END)
    

combination_size = ["", "", "", ""]
possible_numbers = ["1", "2", "3", "4", "5", "6"]

create_game()
