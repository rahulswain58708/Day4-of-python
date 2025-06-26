x=3
match x:
    case 1:
        print("one")
    case 2:
        print("Two")
    case 3:
        print('Three')
    case _:
        print("Unknown number")      #outpu:-Three

name="Rahul"
match name:
    case "Rahul":
        print("Hey Rahul")
    case "Ravi":
        print("Hello Ravi")
    case _:
        print("Who are you?")      #output:-Rahul
