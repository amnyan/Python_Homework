operand = input("Please enter operator(+,-,/,*) ")
number1 = float(input("Please enter first number "))
number2 = float(input("Please enter second number "))
if (operand == "+"):
  print(f"number1 + number2 = {(number1 + number2):.2f}")
elif (operand == "-"):
  print(f"number1 - number2 = {(number1 - number2):.2f}")
elif (operand == "*"):
  print(f"number1 * number2 = {(number1 * number2):.2f}")
elif (operand == "/" ):
    if not number2 == 0:
        print(f"number1 / number2 = {(number1 / number2):.2f}")
    else:
        print("Cann't devide to Zero!!! ")
else:
    print("You write a invalid operand or numbers!!! ")

