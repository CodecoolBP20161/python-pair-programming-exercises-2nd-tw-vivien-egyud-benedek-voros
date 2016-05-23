import datetime


def years(age):
    return datetime.datetime.now().year + 100 - age


def main():
    name = input("Your name: ")
    age = int(input("Your age: "))
    number = int(input("Enter a number:"))
    print(number * (str(years(age)) + "\n"))
    return


if __name__ == '__main__':
    main()
