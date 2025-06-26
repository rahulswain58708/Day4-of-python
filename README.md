📅 Day 4: Today I Learned – match-case in Python 🐍
Topic: Structural Pattern Matching (match-case) – Introduced in Python 3.10

🔍 What I Learned:
Python’s match-case works like switch-case in other languages.

It's used for cleaner, readable conditional branching.

It supports complex pattern matching (like tuples, lists, classes, etc.).

🧠 Syntax:
python
Copy
Edit
value = 2

match value:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Default case")
✅ The _ case is like default – runs when no other pattern matches.

🧪 Practice Example:
python
Copy
Edit
def check_day(day):
    match day:
        case "Monday":
            return "Start of the week!"
        case "Friday":
            return "Weekend is near!"
        case "Sunday":
            return "Rest day 😌"
        case _:
            return "Just another day..."

print(check_day("Friday"))
💡 Key Points:
Available from Python 3.10+

More powerful than simple if-else

Supports matching patterns, destructuring, and guards

📌 TIL Tag: #100DaysOfCode #Python #matchcase #Day4
📁 Repo Idea: Create a match_case_examples.py with mini use cases.
