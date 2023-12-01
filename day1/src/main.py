f = open("day1/input/day1.txt", "r", encoding="utf-8")
words = f.read().split("\n")
STRING_TO_DIGIT = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def find_first_digit(word: str) -> int:
    i = 0
    while i < len(word):
        if word[i].isdigit():
            return int(word[i])
        for digit in STRING_TO_DIGIT:
            if word[i:].startswith(digit):
                return STRING_TO_DIGIT.index(digit)
        i += 1
    return 0


def find_last_digit(word: str) -> int:
    word_r = word[::-1]
    i = 0
    while i < len(word_r):
        if word_r[i].isdigit():
            return int(word_r[i])
        for digit in STRING_TO_DIGIT:
            if word_r[i:].startswith(digit[::-1]):
                return STRING_TO_DIGIT.index(digit)
        i += 1
    return 0


allNum = 0
for word in words:
    print(word)
    number = find_first_digit(word) * 10 + find_last_digit(word)
    print(number)
    allNum += number
print(allNum)
