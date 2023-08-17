board_game= [['','',''],['','',''],['','','']]
symche = ''
def check_symbol():
    global symbol
    symbol = input('Enter symbol : ')
    if symbol == 'x' or symbol=='o':
       
        return True 
    else :
        return False 

def print_board(board_game):
    print('-------------')
    for row in board_game:
        print('|', end='')
        for cell in row:
            print(f' {cell} |', end='')
        print('\n-------------')

    return 'continue playing'   
     

def start_move(board_game,symbol):
    while True:
        try :
           row = int(input('Enter the row (1-3): '))
           if (row > 3 or row <1) :
               print('please enter number between 1,3 :')
               continue
           col = int(input('Enter the col (1-3): '))
           if (col > 3 or col<1) :
               print('please enter number between 1,3 :')
               continue
        except ValueError:
            print('Please enter number between 1,3 :')
            continue
        
        
        if board_game[row-1][col-1] == '' :
            board_game[row-1][col-1] =symbol
            break
        else :
            print('invalid move ,try again ')
            
    print(print_board(board_game)) 
 
def check_win (board_game,symbol):
    for row in range(3):
        if board_game[row][0]== board_game[row][1]== board_game[row][2]==symbol:
            return True 
    for col in range(3):
        if board_game[0][col]== board_game[1][col]== board_game[2][col]==symbol:
            return True
    if (board_game[0][0]== board_game[1][1]== board_game[2][2]==symbol) :
        return True 
    if (board_game[0][2]== board_game[1][1]== board_game[2][0]==symbol) :
        return True 
def check_tie(board_game):
    for row in board_game:
        if '' in row :
            return False
    return True     

def check_turn(symbol):
    global symche
    if symche == symbol:
        return False
    else:
        return True 
    
    
def tic_tac_toe():
    global symche
    print_board(board_game)
    
    while True :
         
         
         if check_symbol():
             pass
         else :
             print('please enter symbol correct is x or o ')
             continue
         if check_turn(symbol):
             pass
         else:
             print('please player turn '+symbol+' other symbol ')
             continue
         start_move(board_game,symbol)
         
         symche = symbol   
         
         if check_win (board_game,symbol):
             print_board(board_game)
             print('player '+ symbol+' wins !')
             break
         if  check_tie(board_game):
             print_board(board_game)
             print('the game ends in a tie !')
             break
    print('to play again, click the run botton ')   

tic_tac_toe()






