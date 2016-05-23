def palindrome(str):
    list_text = [item.lower() for item in list(str)]
    nospace_list_text = []
    for i in range(len(list_text)):
        if list_text[i] != " ":
            nospace_list_text.append(list_text[i])
    return nospace_list_text == nospace_list_text[::-1]


def main():
    text = input("Your text:")
    palindrome(text)
    return


if __name__ == '__main__':
    main()
