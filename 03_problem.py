# vowel or constant
letter=input("Enter a single letter : ")

match letter:
    case 'a'|'e'|'i'|'o'|'u':
        print("it is vowel")
    case _ if letter.isalpha() and len(letter) ==1:
        print("It is constant")
    case _:
        print("invalid input.please enter a single alphabet")