def calculation():
    print("basic calculator")
#input
number1=float(input("enter the first number:" ))
number2 = float(input("enter the second number: "))
#operation
print("operations are")
print("1=addition")
print("2=subtraction")
print("3=multiplication")
print("4=division")
#performation of operation
operation=int(input("enter the operation:"))
if operation == 1:
    answer=number1+number2
    print(f"addition of theese two numbers is :{answer} ")
elif operation == 2:
    answer=number1-number2
    print(f"subtraction of theese two numbers is :{answer} ")
elif operation == 3:
    if number1!=0 and number2!=0:
        answer=number1*number2
        print(f"multiplication of theese two numbers is :{answer} ")
    else:
      print("invalid operation")
elif operation == 4:
    if number1 != 0 and number2 != 0:
        answer=number1/number2
        print(f"division of theese two numbers is :{answer} ")
    else:
      print("invalid operation")
print("end")