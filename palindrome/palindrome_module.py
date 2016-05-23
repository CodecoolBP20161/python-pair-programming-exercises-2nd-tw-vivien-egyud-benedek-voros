def palindrome(str):
    boolean_palindrom = False
    text_list = list(str)
    no_space = []
    for i in range(len(text_list)):
        if text_list[i] != " ":
            no_space.append(text_list[i])
    print(no_space)
    print (no_space[::-1])
    # if no_space.reverse() == no_space:
    #     return boolean_palindrom


def main():
    text = input("Your text:")
    palindrome(text)
    return


if __name__ == '__main__':
    main()
