'''
1 for snake
-1 for water
0 for gun
'''

computer = -1

youDict = {"s": 1, "w": -1, "g": 0}

reverseDict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

youstr = input("ENTER YOUR CHOICE (s/w/g): ")

you = youDict[youstr]

print(f"You chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a draw")

else:
    if(computer == -1 and you == 1):
        print("You Win")

    elif(computer == -1 and you == 0):
        print("You Lose")

    elif(computer == 1 and you == -1):
        print("You Lose")

    elif(computer == 1 and you == 0):
        print("You Win")

    elif(computer == 0 and you == -1):
        print("You Win")

    elif(computer == 0 and you == 1):
        print("You Lose")

    else:
        print("Something went wrong!")