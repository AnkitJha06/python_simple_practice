import random
import string

def pass_gen():
    s1 = string.ascii_letters
    s2 = string.ascii_lowercase
    s3 = string.ascii_uppercase
    s4 = string.punctuation

    try:
        pass_len = int(input("Enter the length of password: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    all_chars = []
    all_chars.extend(list(s1))
    all_chars.extend(list(s2))
    all_chars.extend(list(s3))
    all_chars.extend(list(s4))

    random.shuffle(all_chars)

    password = "".join(all_chars[0:pass_len])

    print(f"Your generated password is: {password}")

pass_gen()