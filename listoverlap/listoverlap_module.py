import random


def listoverlap(list1, list2):
    return sorted(list(set(list1) & set(list2)))


def main():
    a = random.sample(range(30), random.randint(10, 15))
    b = random.sample(range(30), random.randint(10, 15))
    print(listoverlap(a, b))
    return


if __name__ == '__main__':
    main()
