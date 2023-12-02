f = open("day2/input/day2.txt", "r", encoding="utf-8")
games = f.read().split("\n")
games = [game[game.find(":") + 1 :].strip() for game in games]


def part_one(games: list[str]) -> int:
    dict_max = {"red": 12, "green": 13, "blue": 14}
    possible_games = 0
    i = 0
    while i < len(games):
        set_games = games[i].split(";")
        set_games = [set_game.strip() for set_game in set_games]
        possible = True
        for set_game in set_games:
            pull_sets = set_game.split(",")
            pull_sets = [pull_set.strip() for pull_set in pull_sets]
            for pull_set in pull_sets:
                color_sets = pull_set.split(" ")
                if dict_max[color_sets[1]] < int(color_sets[0]):
                    possible = False
        if possible:
            possible_games += i + 1
        i += 1
    return possible_games


def part_two(games: list[str]) -> int:
    number = 0
    for game in games:
        dict = {"red": 0, "green": 0, "blue": 0}
        set_games = game.split(";")
        set_games = [set_game.strip() for set_game in set_games]
        for set_game in set_games:
            pull_sets = set_game.split(",")
            pull_sets = [pull_set.strip() for pull_set in pull_sets]
            for pull_set in pull_sets:
                color_sets = pull_set.split(" ")
                if dict[color_sets[1]] < int(color_sets[0]):
                    dict[color_sets[1]] = int(color_sets[0])
        number += dict["red"] * dict["green"] * dict["blue"]
    return number


print("Part 1: ", part_one(games))
print("Part 2: ", part_two(games))
