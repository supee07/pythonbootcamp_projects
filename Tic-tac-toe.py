import random

def display(board):
    print(f'''
        {board[7]}|{board[8]}|{board[9]}                      7 | 8 | 9
        ---+---+---                     ---+---+----
        {board[6]}|{board[5]}|{board[4]}    positions -->     4 | 5 | 6
        ---+---+---                     ---+---+----
        {board[3]}|{board[2]}|{board[1]}                      1 | 2 | 3
        ''')
def valid_input():
    while True:
        pos = input("enter position:")
        if pos != " " and pos.isalpha () == False :
            if int(pos) in range(1,10) :
                pos=int(pos)
                break
            else:("Not a valid positon")

        else:
            print("Thank you for playing tic tac toe")
            exit()

    return int(pos)

def valid_pos(turn,board):
    print(f'{turn} chance')
    pos = valid_input()
    while True:
        if board[pos] == "   ":
            board[pos] = turn
            break
        else:
            print("Cannot overwrite, please choose new locatin")
            pos = valid_input()

def check(board):
    check = False
    # rows
    if board[1] == board[2] == board[3] != "   " or\
       board[4] == board[5] == board[6] != "   "or\
       board[7]==board[8]==board[9] != "   ":

        check = True
    # col
    elif board[1]==board[4]==board[7] != "   " or \
         board[2]==board[5]==board[8] != "   "  or \
         board[3]==board[6]==board[9] !="   " :

        check = True
    # diagonals 159 357
    elif board[1]==board[5]==board[9] != "   " or \
         board[3]==board[5]==board[7] != "   ":

        check = True
    return check


def userip(board,symbol):
    sym1,sym2= symbol[random.randint(0,1)]
    #print(sym1,sym2)
    print(f'{sym1} is going first\n\n')
    for i in range(9):
        if i%2==0:
            turn =' '+sym1+' '
            valid_pos(turn,board)
        else:
            turn= " "+sym2+" "
            valid_pos(turn,board)
        display(board)
        #print(board)
        if i >= 4:
            if check(board) :
                display(board)
                print(f'{turn} WON! congrats!!')

                break
        if i == 8 :
            print("None WON , It's a TIE!")


def game():
    board=[ "--", "   " , "   ","   ","   ","   ","   ","   ","   ","   "]
    #print(len(board))
    symbol = [("X","O"),("O","X")]
    display(board)
    while True:
        marker = input("\nEnter your marker").upper()
        if marker == "O" or marker == 'X':
            userip(board,symbol)
            break
        else:
            print("Wrong marker(O,X),please enter again")

def main():
    again = "Y"
    while again == "Y":
        print('''***---Let's play tic-tac-toe!!!-----****
    if you want to quit press [space]
    GOOD LUCK !!!!''')
        print()
        print()
        game()

        again = input("Press Y/y for playing again").upper()

main()


  
