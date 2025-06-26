color = input("Enter traffic light color (red/yellow/green): ").lower()

match color:
    case "red":
        print("Stop!")
    case "yellow":
        print("Wait!")
    case "green":
        print("Go!")
    case _:
        print("Invalid color. Please enter red, yellow, or green.")
