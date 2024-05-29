import random

def dice_roll(d,r):
    result=[]
    for i in range(rolls):
        result.append(random.randint(1,dice))
    return result

ch=1
while (ch==1):
    try:
        dice=int(input("Enter no. of sides of dice: "))
        rolls=int(input("Enter no. of rolls: "))
        if(dice<0 or rolls<0):
            print("You need to enter a positive no.!")
        else:
            
            l=dice_roll(dice,rolls)
            print("Displaying your results:")
            for i in range(len(l)):
                print("Roll "+str(i+1)+": ",l[i])

    except ValueError:
        print("You need to enter a valid positive no.!")

    try:
        ch=int(input("Do you want to play more(1=Yes/0=No): "))
        if ch not in[1,0]:
            print("Invalid input. Exiting the program.")
            break
    except ValueError:
        print("Invalid input. Exiting the program.")
        break

print("Thank You!")
