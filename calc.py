a = int(input("say an integer: "))
b = int(input("say an integer: "))

operator = input("what shall I do with these numbers?: ")

"""if operator == "*":
    print (a*b)
elif operator in ":/":
    print (a/b)
elif operator == "+":
    print (a+b)
elif operator == "-":
    print (a-b)

"""

match operator:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "/":
        print(a/b)
    case "*":
        print(a*b)
    
