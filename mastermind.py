from random import choice

combination_size = ["", "", "", ""]
# possible_colors = ["🔴", "🟠", "🟡", "🟢", "🔵", "🟣"]
# possible_colors = ["\U+1F534", "\U+1F7E0", "\U+1F7E1", "\U+1F7E2", "\U+1F535", "\U+1F7E3"]
possible_numbers = ["1", "2", "3", "4", "5", "6"]
number_of_attempts = 10
combination = []

def create_combination(combination_size, possible_numbers, combination):
    combination = []
    for _ in combination_size:
        combination += choice(possible_numbers)
    print(combination)
    return combination

create_combination(combination_size, possible_numbers, combination)

