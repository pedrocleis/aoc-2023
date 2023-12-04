import math

f = open("inputs/day3.txt", "r", encoding="utf-8")
words = f.read().split("\n")


def part_one(words: list[str]) -> int:
    numbers = []
    numbers_to_check = []
    i = 0
    while i < len(words):
        j = 0
        isNumber = False
        number = ""
        first_digit = True
        while j < len(words[i]):
            if words[i][j].isdigit():
                number = number + words[i][j]
                isNumber = True
                if first_digit:
                    init_number = [i, j]
                    first_digit = False
            elif not words[i][j].isdigit() and isNumber:
                numbers.append(int(number))
                search_numbers = [init_number[0], init_number[1], i, j]
                if search_numbers[0] != 0:
                    search_numbers[0] -= 1
                if search_numbers[1] != 0:
                    search_numbers[1] -= 1
                if search_numbers[2] != len(words) - 1:
                    search_numbers[2] += 1
                k = search_numbers[0]
                l = search_numbers[1]
                while k <= search_numbers[2]:
                    l = search_numbers[1]
                    while l <= search_numbers[3]:
                        if not words[k][l].isdigit() and not words[k][l] == ".":
                            numbers_to_check.append(int(number))
                        l += 1
                    k += 1
                number = ""
                isNumber = False
                first_digit = True
            if isNumber and j == len(words[i]) - 1:
                numbers.append(int(number))
                search_numbers = [init_number[0], init_number[1], i, j]
                if search_numbers[0] != 0:
                    search_numbers[0] -= 1
                if search_numbers[1] != 0:
                    search_numbers[1] -= 1
                if search_numbers[2] != len(words) - 1:
                    search_numbers[2] += 1
                k = search_numbers[0]
                l = search_numbers[1]
                while k <= search_numbers[2]:
                    l = search_numbers[1]
                    while l <= search_numbers[3]:
                        if not words[k][l].isdigit() and not words[k][l] == ".":
                            numbers_to_check.append(int(number))
                        l += 1
                    k += 1
            j += 1
        i += 1
    return sum(numbers_to_check)


def part_two(words: list[str]) -> sum:
    numbers = []
    positions = []
    i = 0
    while i < len(words):
        j = 0
        isNumber = False
        number = ""
        first_digit = True
        while j < len(words[i]):
            if words[i][j].isdigit():
                number = number + words[i][j]
                isNumber = True
                if first_digit:
                    init_number = [i, j]
                    first_digit = False
            elif not words[i][j].isdigit() and isNumber:
                numbers.append(int(number))
                search_numbers = [init_number[0], init_number[1], i, j]
                if search_numbers[0] != 0:
                    search_numbers[0] -= 1
                if search_numbers[1] != 0:
                    search_numbers[1] -= 1
                if search_numbers[2] != len(words) - 1:
                    search_numbers[2] += 1
                positions.append(search_numbers)
                number = ""
                isNumber = False
                first_digit = True
            if isNumber and j == len(words[i]) - 1:
                numbers.append(int(number))
                search_numbers = [init_number[0], init_number[1], i, j]
                if search_numbers[0] != 0:
                    search_numbers[0] -= 1
                if search_numbers[1] != 0:
                    search_numbers[1] -= 1
                if search_numbers[2] != len(words) - 1:
                    search_numbers[2] += 1
                positions.append(search_numbers)
                number = ""
                isNumber = False
            j += 1
        i += 1

    return_ratio = 0
    i = 0
    while i < len(words):
        j = 0
        while j < len(words[i]):
            if words[i][j] == "*":
                numbers_ratio = []
                k = 0
                while k < len(positions):
                    if i in range(positions[k][0], positions[k][2] + 1) and j in range(
                        positions[k][1],
                        positions[k][3] + 1,
                    ):
                        numbers_ratio.append(int(numbers[k]))
                    k += 1
                if len(numbers_ratio) == 2:
                    return_ratio += math.prod(numbers_ratio)
            j += 1
        i += 1
    return return_ratio


print(part_one(words))
print(part_two(words))
