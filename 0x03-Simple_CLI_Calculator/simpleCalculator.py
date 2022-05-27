https://drive.google.com/file/d/1YRE80YTBwYqn_FXMyGhzRGWkk64O1ltk/view?usp=sharing


operation = input('''Please type in the math operation you would like to perform:
+ for addition
- for subtraction
* for multiplication
/ for division
% for modulo
''')

number1 = int(input("Input the first number: "))
number2 = int(input("Input the second number: "))

if operation=='+':
    add= number1+number2
    print(add)

elif operation=='-':
    subtract = number1-number2
    print(subtract)

elif operation=='*':
    multiply= number1*number2
    print(multiply)

elif operation=='/':
    divide = number1/number2
    print(divide)

elif operation=='%':
    remainder= number1%number2
    print(remainder)

else:
    print('you have not typed the valid operator, please run the program again. ')


