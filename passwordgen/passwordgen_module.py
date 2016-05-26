import random
import string


def passwordgen():
    password_list = [""] * 8
    for i in range(8):
        password_list[i] = random.choice(
            string.ascii_uppercase +
            string.ascii_lowercase +
            string.digits +
            r"[!@#$%^&*()?]")
    random_list = random.sample(range(0, 8), 4)
    password_list[random_list[0]] = random.choice(string.ascii_uppercase)
    password_list[random_list[1]] = random.choice(string.ascii_lowercase)
    password_list[random_list[2]] = random.choice(string.digits)
    password_list[random_list[3]] = random.choice(r"[!@#$%^&*()?]")
    joined_list = "".join(password_list)
    return(joined_list)


def main():
    passwordgen()
    return


if __name__ == '__main__':
    main()
