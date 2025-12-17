#calculator program

num1=float(input("Enter the first number: "))
operator=input("Enter the operator (+,-,*,/,^,√,%) : ")
num2=float(input("Enter the second number: "))

if operator=='+':
    print(num1,"+",num2, "=" ,num1+num2)
elif operator=='-':
    print(num1,"-",num2, "=" ,num1-num2)
elif operator=='*':
    print(num1,"*",num2,"=" ,num1*num2)
elif operator=="/":
    if num2==0 :
        print("error! [cannot divide by zero]")
    else:
        print(num1,"/",num2, "=" ,num1/num2)
elif operator=="^":
    print(num1,"^",num2,"=" ,num1**num2)
elif operator=='√':
    print("The square root of ",num1, "is",num1**0.5)
elif operator=='%':
    print(num1,"%",num2, "=" ,(num1/100)*num2)

