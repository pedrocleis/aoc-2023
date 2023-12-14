f = open("inputs/day4.txt", "r", encoding="utf-8")
games = f.read().split("\n")


def part_one(games: list[str]) -> int:
    points = 0
    for game in games:
        game = game[game.find(":") + 1 :].strip()
        game_numbers = game.split("|")
        game_numbers = [game_number.strip() for game_number in game_numbers]
        i = 0
        have_numbers = game_numbers[1].split(" ")
        winning_numbers = game_numbers[0].split(" ")
        while "" in have_numbers:
            have_numbers.remove("")
        while "" in winning_numbers:
            winning_numbers.remove("")
        numbers_won = 0
        while i < len(have_numbers):
            if have_numbers[i] in winning_numbers:
                numbers_won += 1
            i += 1
        if numbers_won > 1:
            points += 2 ** (numbers_won - 1)
        else:
            points += numbers_won
    return points


def part_two(games: list[str]) -> int:
    cards = [0] * len(games)
    i = 0
    while i < len(games):
        games[i] = games[i][games[i].find(":") + 1 :].strip()
        game_numbers = games[i].split("|")
        game_numbers = [game_number.strip() for game_number in game_numbers]
        j = 0
        have_numbers = game_numbers[1].split(" ")
        winning_numbers = game_numbers[0].split(" ")
        while "" in have_numbers:
            have_numbers.remove("")
        while "" in winning_numbers:
            winning_numbers.remove("")
        numbers_won = 0
        while j < len(have_numbers):
            if have_numbers[j] in winning_numbers:
                numbers_won += 1
            j += 1

        winning_numbers_card = numbers_won
        cards[i] += 1
        number_of_cards = cards[i]
        k = 0
        while k < number_of_cards:
            j = i + 1
            winning_numbers_card = numbers_won
            while j < len(games) and winning_numbers_card > 0:
                cards[j] += 1
                j += 1
                winning_numbers_card -= 1
            k += 1
        i += 1
    return sum(cards)


print(part_two(games))
