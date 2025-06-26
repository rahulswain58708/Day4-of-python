marks = int(input("Enter your marks (0-100): "))

match marks:
    case _ if marks >= 90:
        print("Grade: A")
    case _ if marks >= 75:
        print("Grade: B")
    case _ if marks >= 50:
        print("Grade: C")
    case _ if marks >= 0:
        print("Grade: F")
    case _:
        print("Invalid input! Please enter marks between 0 and 100.")
