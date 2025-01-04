def pl_acc(): # accepts the players choice
    ply1=input("Enter player 1 choice 'x' or 'o' :")   ### letters ke case me dikat ho sakta ahi
    if ply1=="x":       
        ply2="o"
    elif ply1=="o":
        ply2="x"
    else:
        print("Enter Valid choice")
        pl_acc() # recall itself function if character other than 'x' or 'o' is enterd 
    return ply1,ply2 #returns players choice
    

def create_grid(): # creates the initial grid
    brd=[[".",".","."],
         [".",".","."],
         [".",".","."]]
    return brd
    
def fill(count,board,player_1,player_2):  #main working of the game
    l=win(board)  #checks wheather either player has won or not
    if(l=='false'):  #executes furthur game if no one has wonc
        if(count<10):  #limit the total response from the player
            if count==1:  #print the initial starting grid
                cd=0
                for r in range(0,3):
                    print(board[r][0], " |", board[r][1], "|", board[r][2])
                    if(cd!=2):
                        print("---+---+---")
                    cd+=1
            row,col=accp(count,board,player_1,player_2)  # calls accp() to accept row and columnn fom the user
            if (board[row][col]=="."):  #checks wheather the positin is occupied or not
                if(count%2==1):  #gives chance to players one by one
                    board=change(board,row,col,player_1)
                    
                else:
                    board=change(board,row,col,player_2)
                
                count+=1  # update the total responses by both the players
                c=0
                for r in range(0,3):  # print the updated game
                    print(board[r][0], " |", board[r][1], "|", board[r][2])
                    if(c!=2):
                        print("---+---+---")
                    c+=1
            else:   # executes when positin is already filled
                c=0
                for r in range(0,3):
                    print(board[r][0], " |", board[r][1], "|", board[r][2])
                    if(c!=2):
                        print("---+---+---")
                    c+=1
                print("The position is already taken enter another position")  
            fill(count,board,player_1,player_2)  # goes for next player to play
        else:
            print("Game is over its a draw")
    elif(l=='won'):
        pass
    
def change(brad,row,col,ply):  # mark the player's choice
    brad[row][col]=ply
    return brad
def accp(count,board,player_1,player_2):   # accepts the row and cloumn by the user
    if count%2==1:
        p="player-1"
    else:
        p="player-2"
    row=int(input(f"{p} Enter the row number --> :"))
    col=int(input(f"{p} Enter the column number  :"))
    if (row>=0 and row<3 and col>=0 and col<3):  # checks the entered row and column are in desired range or not
        return row,col
    
    else:   #executes the row and column is not in the desired range
        print("Enter row and column number from 0 to 2 ")
        accp(count,board,player_1,player_2)    #recalls itself if the entered row and column is not in the range
        
   
def win(board):  #checks who is winning
    w="false"
    for i in range(0,3):  
        if(board[i][0]==board[i][1]==board[i][2]=='x'): #for row 'x'
            w="won"
            print(f"player 'x'wins the game")
        if(board[i][0]==board[i][1]==board[i][2]=='o'): #for row 'o'
            w="won"
            print(f"player 'o'wins the game")
        if(board[0][i]==board[1][i]==board[2][i]=='x'): #for cloumn 'x'
            w="won"
            print(f"player 'x' wins the game")
        if(board[0][i]==board[1][i]==board[2][i]=='o'): #for cloumn 'o'
            w="won"
            print(f"player {board[1][i]} wins the game")
    
    if(board[0][0]==board[1][1]==board[2][2]=='x'):  #for diagonal 'x'
        w="won"
        print(f"player'x'wins the game")
    if(board[0][0]==board[1][1]==board[2][2]=='o'): #for diagonal 'o'
        w="won"
        print(f"player'o' wins the game")
    if(board[0][2]==board[1][1]==board[2][0]=='x'):  #for back diagonal 'x'
        w="won"
        print(f"player 'x' wins the game")
    if(board[0][2]==board[1][1]==board[2][0]=='o'): #for back diagonal 'o'
        w="won"
        print(f"player 'o' wins the game")
    return w
        
    
    
        
def main():  
    print("Lets play the game")
    count=1
    player1,player2=pl_acc()  #pass the players choice
    board=create_grid()   # calls the initial grid
    fil= fill(count,board,player1,player2)  #calls the fill() to start the game
main()  
