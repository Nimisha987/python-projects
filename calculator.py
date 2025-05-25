numbers1=float(input("Enter number: "))
numbers2=float(input("Enter number2 : "))
operation=input("+,-,*,/ : ")
if operation == "+":
    result=numbers1+numbers2
    print(result)
elif operation=="-":
    result=numbers1-numbers2
    print(result)
elif operation=="*":
    result=numbers1*numbers2
    print(result)
elif operation=="/":
    result=numbers1/numbers2
    print(result)
else:
    print("Invalid operator")
