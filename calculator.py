def add(c, d):
    return c + d
def subtract(c, d):
    return c - d
def multiply(c, d):
    return c* d
def divide(c, d):
    return c / d
    print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
select = int(input("Select operations form 1, 2, 3, 4 :"))
c = int(input("Enter first number: "))
d = int(input("Enter second number: "))
if select == 1:
    print(c, "+", d, "=",
                    add(c, d)) 
elif select == 2:
    print(c, "-", d, "=",
                    subtract(c, d))
elif select == 3:
    print(c, "*", d, "=",
                    multiply(c,d))
elif select == 4:
    print(c, "/", d, "=",
                    divide(c, d))
else:
    print("Invalid input")