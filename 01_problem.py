# Day Name Finder
number=int(input("Enter a number (1-7) : "))
match number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednessday")
    case 4:
        print("Thuersday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("invalid number")