# Initialize players' names
player_x=str(input("X player Name: ").strip().capitalize())
player_o=str(input("O player Name: ").strip().capitalize())

# Initialize the game board
def Game_Board():
    global game_shape
    game_shape = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    for row in game_shape:
        print(' | '.join(row))
        print('-' * 9)

# Initialize X player
def x (a,b): 
    game_shape[a][b] = 'x'
    for x in game_shape:
        print (x) 


# Initialize O player
def o (a,b): 
    game_shape[a][b] = 'o'
    for o in game_shape:
        print (o)
    
# Function to check for a win
def check_win ():
    if game_shape[0][0] == 'x' and game_shape[0][1] == 'x' and game_shape[0][2] == 'x': 
        return 'x'
    if game_shape[1][0] == 'x' and game_shape[1][1] == 'x' and game_shape[1][2] == 'x':
        return 'x'
    if game_shape[2][0] == 'x' and game_shape[2][1] == 'x' and game_shape[2][2] =='x':
        return 'x'
    if game_shape[0][0] == 'x' and game_shape[1][0] == 'x' and game_shape[2][0]== 'x' :  
        return 'x'
    if game_shape[0][1] == 'x' and game_shape[1][1] == 'x' and game_shape[2][1]== 'x' : 
        return 'x'
    if game_shape[0][2] == 'x' and game_shape[1][2] == 'x' and game_shape[2][2]== 'x' :
        return 'x'
    if game_shape[0][0] == 'x' and game_shape[1][1] == 'x' and game_shape[2][2]== 'x' :  
        return 'x'
    if game_shape[0][2] == 'x' and game_shape[1][1] == 'x' and game_shape[2][0]== 'x' : 
        return 'x'
#--------------------------------------------------------------------------------------#
    if game_shape[0][0] == 'o' and game_shape[0][1] == 'o' and game_shape[0][2] == 'o': 
        return 'o'
    if game_shape[1][0] == 'o' and game_shape[1][1] == 'o' and game_shape[1][2] == 'o':
        return 'o'
    if game_shape[2][0] == 'o' and game_shape[2][1] == 'o' and game_shape[2][2] =='o':
        return 'o'
    if game_shape[0][0] == 'o' and game_shape[1][0] == 'o' and game_shape[2][0] == 'o' :  
        return 'o'
    if game_shape[0][1] == 'o' and game_shape[1][1] == 'o' and game_shape[2][1] == 'o' : 
        return 'o'
    if game_shape[0][2] == 'o' and game_shape[1][2] == 'o' and game_shape[2][2] == 'o' :
        return 'o'
    if game_shape[0][0] == 'o' and game_shape[1][1] == 'o' and game_shape[2][2]== 'o' :  
        return 'o'
    if game_shape[0][2] == 'o' and game_shape[1][1] == 'o' and game_shape[2][0]== 'o' : 
        return 'o'
    
def check_draw():
    for row in game_shape:
        if ' ' in row:
            return False
    return True

Game_Board()

while True:
    try:

        while True:
            print("\n")
            print(player_x)
            print("\n")
            a = int(input("Enter the row number (1-3) > "))
            b = int(input("Enter the column number (1-3) > "))
            if  game_shape[a-1][b-1] == ' ':
                x(a-1,b-1)
                break
            else:
                print('------------------------------------------That square is already taken. Try again------------------------------------------')
                print("\n")
                continue

        if check_win() == 'x':
            print("\n")
            print(f'------------------------------------------ {player_x} is win ------------------------------------------')
            break

        if check_draw():
            print("\n")
            print('------------------------------------------ It\'s a draw! ------------------------------------------')
            break        

        while True:
            print("\n")
            print(player_o)
            print("\n")
            a = int(input("Enter the row number (1-3) > "))
            b = int(input("Enter the column number (1-3) > "))   
            if game_shape[a-1][b-1] == ' ':
                o(a-1,b-1)
                break
            else:
                    print('------------------------------------------That square is already taken. Try again------------------------------------------')
                    print("\n")
                    continue 
           
        if check_win() == 'o':
            print("\n")
            print(f'------------------------------------------{player_o} is win------------------------------------------')
            break
        
        if check_draw():
            print("\n")
            print('------------------------------------------ It\'s a draw! ------------------------------------------')
            break 

    except :
        print("\n")
        print("You should add number between 1 and 3")
        print("End Game")
        break
