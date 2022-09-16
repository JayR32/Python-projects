import string
import random

alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list ("!@#$%^&*()_+}{:<>?,./")
characters = list (string.ascii_letters + string.digits + "!@#$%^&*()")
def generate_random_password():

    length = int(input("Enter password length in num :)"))

    alphabets_length = int(input("Enter letter count :)"))

    digits_length = int(input("Enter numbers count :)"))

    special_characters_length = int(input("Enter special character count :)"))

    Characters_Length = alphabets + digits + special_characters + characters

    if Characters_Length > length:
        print("characters total count is greater than the password length :(")
        return
    password = []
    for i in range(alphabets_length):
        password.append(random.choice(alphabets))

    for i in range(digits_length):
        password.append(random.choice(digits))

    for i in range(special_characters_length):
        password.append(random.choice(special_characters))

    if Characters_Length < length:
        random.shuffle(characters)
        for i in range(length - Characters_Length):
            password.append(random.choice(characters))
        

    print("".join(password))

generate_random_password ()