#Simple Calculator

#MENU
print("VALID OPERATIONS\n")
print("1. Addition (+)\n2. Subtraction (-1)\n3. Multiplication (*)\n4. Division (/) ")
ch=1
while(ch):
    a=int(input("Enter first operand: "))
    b=int(input("Enter second operand: "))
    op=int(input("Enter the corresponding serial no. of the operator you want to choose: "))
    if(op==1):
        print("You chose Addition operation")
        print("Result=",a+b)
    elif(op==2):
        print("You chose Subtraction operation")
        print("Result=",a-b)
    elif(op==3):
        print("You chose Multiplication operation")
        print("Result=",a*b)
    elif(op==4):
        print("You chose Division operation")
        print("Result=",a/b)
    else:
        print("You entered invalid operator!!")
    ch=("Do you want to perform more calculation?(1:Yes, 0:No): ")
print("Thank You!")