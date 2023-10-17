import calculator

selection = int(input("\nSelect your calculator operation:\
                      \n1. Addition\
                      \n2. Subtraction\
                      \n3. Multiplication\
                      \n4. Division\n"))

num1 = int(input("\nProvide your first value:"))
num2 = int(input("\nProvide your second value:"))

if selection ==1:
    answer = calculator.calculate(num1,num2,"+")
    print(f"{num1}+{num2}={answer}")
elif selection ==2:
    answer = calculator.calculate(num1,num2,"-")
    print(f"{num1}-{num2}={answer}")
elif selection ==3:
    answer = calculator.calculate(num1,num2,"*")
    print(f"{num1}*{num2}={answer}")
elif selection ==4:
    if num2!=0:
        answer = calculator.calculate(num1,num2,"/")
        print(f"{num1}/{num2}={answer}")
    else: print("Cannot divide by 0")
else:
    print("You have selected an invalid calculator operation.")