# Calculator
print("welcome to calculator")
numb1=int(input("Enter First number:"))
numb2=int(input("Enter second number:"))
print("Chose operator +,-,*,%,/,")
operator=input("Enter a operator:")
match operator:
    case "+":
        print("Sum is:",numb1+numb2)
    case "-":
        print("Difference is:",numb1-numb2)
    case "*":
        print("multiplication is:",numb1*numb2)
    case "%":
        print("Module is :",numb1%numb2)
    case "/":
        print("Division is:",numb1/numb2)
    case _:
        print("Invalid Operator please chose correct operator")
