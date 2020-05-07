import random

from settings import \
    FLITN, \
    MIN_NAME_LENGTH, \
    MAX_NAME_LENGTH, \
    VOWELS, \
    CONSONANTS, \
    MAIN_LETTERS, \
    NAME_ENDING_MALE, \
    SURNAME_ENDING_MALE, \
    MIN_SURNAME_LENGTH, \
    MAX_SURNAME_LENGTH

# Variables
drop_rate = 0  # Коэффицент вероятности выпадения гласных или согласных букв


# Генерация первой буквы в имени
def first_letter():
    global drop_rate
    fl = random.choice(FLITN)
    if fl in VOWELS:
        drop_rate = 2
    else:
        drop_rate = 9
    return fl


# Генерация последующих букв
def next_letter(pl):
    prob = random.randint(1, 10)
    if pl in VOWELS and prob > 1:
        nl = random.choice(CONSONANTS)
    elif pl in CONSONANTS and prob < 10:
        nl = random.choice(VOWELS)
    else:
        nl = random.choice(MAIN_LETTERS)
    if nl == pl:
        return next_letter(nl)
    return nl


# Генерация окончания в имени
def last_letter(pl, ending):
    ll = random.choice(ending)
    if ll[0] == pl:
        return last_letter(pl, ending)
    return ll


# Генерация длины имени
def name_length(min_, max_):
    return random.randint(min_, max_)


# Генератор имени
def name_generator():
    length = name_length(MIN_NAME_LENGTH, MAX_NAME_LENGTH)
    name = first_letter()
    for x in range(length - 2):
        char = next_letter(name[-1])
        name += char
    name += last_letter(name[-1], NAME_ENDING_MALE)
    return name.title()


# Генаратор фамилии
def surname_generator():
    length = name_length(MIN_SURNAME_LENGTH, MAX_SURNAME_LENGTH)
    surname = first_letter()
    for x in range(length):
        char = next_letter(surname[-1])
        surname += char
    surname += last_letter(surname[-1], SURNAME_ENDING_MALE)
    return surname.title()
