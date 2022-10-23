"""Creating tic tac toe game"""
import random
def move():
    print("Select turn order. Make '0' or '1'")
    m = random.randrange(0,2)
    ss = input("When you are ready to start, click? 'y'")
    if m == 0 and ss == 'y':
        print("For crosses plays '0'" )
    else:
        print("For crosses plays '1'" )
def move_1():
    if  not((board[0][0]=='0' and board[0][1] =='0' and board[0][2]=='0') or\
        (board[1][0]=='0' and board[1][1] =='0' and board[1][2]=='0') or\
        (board[2][0]=='0' and board[2][1] =='0' and board[2][2]=='0') or\
        (board[0][0]=='0' and board[1][1] =='0' and board[2][2]=='0') or\
        (board[0][2]=='0' and board[1][1] =='0' and board[2][0]=='0') or\
        (board[0][0]=='0' and board[1][0] =='0' and board[2][0]=='0') or\
        (board[0][1]=='0' and board[1][1] =='0' and board[2][1]=='0') or\
        (board[0][2]=='0' and board[1][2] =='0' and board[2][2]=='0')):
        a, b = input("Move player One \nChoose a line: '0', '1', '2'\nChoose a column: '0', '1', '2' "),  input()
        if (b == '0') or (b == '1') or (b =='2'):
            board[int(a)][int(b)]='X'
            board_conclusion()
            move_2()
        else: 
            print("Input is invalid, try again")
            move_1()
        
    else: 
        print('zeroes won')


def move_2():
    if  not((board[0][0]=='X' and board[0][1] =='X' and board[0][2]=='X') or\
    (board[1][0]=='X' and board[1][1] =='X' and board[1][2]=='X') or\
    (board[2][0]=='X' and board[2][1] =='X' and board[2][2]=='X') or\
    (board[0][0]=='X' and board[1][1] =='X' and board[2][2]=='X') or\
    (board[0][2]=='X' and board[1][1] =='X' and board[2][0]=='X') or\
    (board[0][0]=='X' and board[1][0] =='X' and board[2][0]=='X') or\
    (board[0][1]=='X' and board[1][1] =='X' and board[2][1]=='X') or\
    (board[0][2]=='X' and board[1][2] =='X' and board[2][2]=='X')):
        c,d = input("Move player Two \nChoose a line: '0', '1', '2' \nChoose a column: '0', '1', '2'  "), input()
        if ((c == '0') or (c == '1') or (c =='2') and (d == '0') or (d == '1') or (d =='2')) and (board[int(c)][int(d)]!='0'or board[int(c)][int([d])]!='X'):
                board[int(c)][int(d)]="0"
                board_conclusion()
                move_1()
        else:
            print("Input is invalid, try again")
            move_2()
    else:
        print("crowses won")
def board_conclusion():
    print(f'{board[0][0]} {board[0][1]} {board[0][2]}')
    print(f'{board[1][0]} {board[1][1]} {board[1][2]}')
    print(f'{board[2][0]} {board[2][1]} {board[2][2]}')            
board = [['-','-','-'],['-','-','-'],['-','-','-']]
move_1()