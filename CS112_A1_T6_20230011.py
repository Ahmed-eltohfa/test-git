# Description : connect 4 is a 2-player game the players try to get 4 cards in order to win
# Author: Ahmed Ehab Salah Elden (ID:20230011)
# Version: V1.3
# Date : Feb 29 2024

# setteing coulmns variables and a variable that holds them all
co1=["-","-","-","-","-","-"]
co2=["-","-","-","-","-","-"]
co3=["-","-","-","-","-","-"]
co4=["-","-","-","-","-","-"]
co5=["-","-","-","-","-","-"]
co6=["-","-","-","-","-","-"]
co7=["-","-","-","-","-","-"]
cAll=[co1,co2,co3,co4,co5,co6,co7]

# make a function that returns an empty var to assign it to the main variable(cAll)
def emptyBoard():
    co1=["-","-","-","-","-","-"]
    co2=["-","-","-","-","-","-"]
    co3=["-","-","-","-","-","-"]
    co4=["-","-","-","-","-","-"]
    co5=["-","-","-","-","-","-"]
    co6=["-","-","-","-","-","-"]
    co7=["-","-","-","-","-","-"]
    cAll=[co1,co2,co3,co4,co5,co6,co7]
    return cAll

# making a function that prints the board depending on the main var with a good visualization
def printBoard():
    print("\n\n")
    for i in range(6):
        for j in range(7):
            print("## ##",end="") if j<6 else print("## ##")
        row=[]
        for j in range(7):
            row.append(cAll[j][i])
            # print(row)
        for j in range(7):
            print("|",row[j],"|",end="") if j<6 else print("|",row[j],"|")
        row=[]
    for i in range(7):
        print(f"# {i+1} #",end="") if i<6 else print(f"# {i+1} #")
    print("\n\n")

# a function that returns true if a player win and false othewise
def checkWin():
    count=1
    # check win in the same coulmn
    for i in range(7):
        for j in range(5):
            if cAll[i][j] == cAll[i][j+1] and cAll[i][j] != "-":
                count+=1
            else:count=1
            if count==4:
                return True
            
    
    # check win in the same row and do the
    count = 1
    for i in range(6):
        for j in range(6):
            if cAll[j][i] == cAll[j+1][i] and cAll[j][i] != "-":
                count+=1
            else:count=1
            if count == 4:
                return True
    
    # check win diagonally
    
    # for every coulmn
    for i in range(7):
        # for every row
        for j in range(6):
            count = 1
            # for the next 4 diagonally
            for k in range(1,5+1):
                if j+k > 5 or i+k > 6: 
                    count =1
                    break
                # print(f"i=>{i}, j=>{j}, k=>{k}")
                if cAll[i][j] == cAll[i+k][j+k] and cAll[i][j] != "-":
                    count +=1
                    # print("ezdad")
                else:count = 1
                if count == 4:
                    return True
            count = 1

            # for the previous 4 diagonally
            for k in range(1,5+1):
                tempCo = 7-i-1
                if j+k > 5 or tempCo-k > 6: 
                    count =0
                    break
                if cAll[tempCo][j] == cAll[tempCo-k][j+k] and cAll[tempCo][j] != "-":
                    count +=1
                else:count = 1
                if count == 4:
                    return True
            count = 1
    return False

# main code

print("***Welcome to connect 4 game to put the card choose the coulmn you want to put the card in***\n")
print("***you have to connect 4 card in the same row or column or diagonal to win***")
symbol1 = input("Player 1 please insert your charachter (card char): ").lower()
# check the symbol is one charchter
while len(symbol1) > 1:
    symbol1 = input("Player 1 please insert one char: ").lower()

symbol2 = input("Player 2 please insert your charachter (card char): ").lower()
while len(symbol2) > 1:
    symbol2 = input("Player 2 please insert one char: ").lower()

# make sure the two symbols are not the same
while symbol2 == symbol1:
    symbol2 = input("Player 2 choose another char: ").lower()

while True:
    printBoard()
    # player one turn
    p1=int(input("Player 1 choose coulmn: "))
    # check if the column is avilable or not
    while p1 < 0 or p1 > 7 or cAll[p1-1][0] != "-":
        p1=int(input("Player 1 choose a vaild number: "))
    # change the the choosen place to the symbol
    for i in range(5,-1,-1):
        if cAll[p1-1][i] == "-":
            cAll[p1-1][i] = symbol1
            break
        else: continue
    # check if the player win and give him the choice to raplay
    if checkWin():
        printBoard()
        print("Congratz player 1 you are the winner ;)")
        again = input("A) Play again\nB) Exit\n").lower()
        while again not in list("ab"):
            again = input("Enter a valid choice: ").lower()
        if again == "a":
            cAll = emptyBoard()
            continue
        else:
            break
    else:printBoard()
    
    # player two turn and do the same 
    p2=int(input("Player 2 choose coulmn: "))
    while p2 < 0 or p2 > 7 or cAll[p2-1][0] != "-":
        p2=int(input("Player 2 choose a vaild number: "))
    for i in range(5,-1,-1):
        if cAll[p2-1][i] == "-":
            cAll[p2-1][i] = symbol2
            break
        else: continue
    if checkWin():
        printBoard()
        print("Congratz player 2 you are the winner ;)")
        again = input("A) Play again\nB) Exit\n").lower()
        while again not in list("ab"):
            again = input("Enter a valid choice: ").lower()
        if again == "a":
            cAll = emptyBoard()
            continue
        else:break
    else:printBoard()
print("Thx for playing")