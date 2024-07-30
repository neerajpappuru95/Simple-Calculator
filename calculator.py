num1 = input("Enter a number: ")
variable = input("Choose the Operations(+, -, *, /, %): ")
num2 = input("Enter a number: ")

add = float(num1) + float(num2)
subtract = float(num1) - float(num2)
multiply = float(num1) * float(num2)
divide = float(num1) / float(num2)
modulus = float(num1) % float(num2)

if variable == "+":
    print(add)

elif variable == "-":
    print(subtract)

elif variable == "*":
    print(multiply)

elif variable == "/":
    print(divide)

elif variable == '%':
    print(modulus)

else:
    print("Error: Invalid input operation!!")

