def TTT():
#FIRST EDIT TO PUSH BRANDON COMMENT 100
#Second edit to push- Bryan
#Bryan is cool

#This is a cool program- Bryan
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    "I set all the possible winning combinations so that I can easily see if any player has appropriate winning moves"
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


#Displaying a tic tac toe board that I initiated in the previous function
    def displayBoard():
        print(board[0],"|", board[1],"|", board[2])
        print("---------")
        print(board[3],"|", board[4],"|", board[5])
        print("---------")
        print(board[6],"|", board[7],"|", board[8])
        print()

#Player one chooses a move and we use the checkMove function inside this function to test if the move will work or not
    def player1():
        n = checkMove()
        if board[n] == "X" or board[n] == "O":
            print("\nYou cannot move there. Choose again.")
            player1()
        else:
            board[n] = "X"

#Player two chooses a move and we use the checkMove function inside this function to test if the move will work or not
    def player2():
        n = checkMove()
        if board[n] == "X" or board[n] == "O":
            print("\nYou cannot move there. Choose again.")
            player2()
        else:
            board[n] = "O"

#This is the function I referred to before in the previous two functions to see if the players moves are legal
    def checkMove():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nThat's not on the board. Try again")
                        continue
                except ValueError:
                   print("\nPlease enter a number.")
                   continue


#This function sees if any player has won or if the game was a tie
    def check_board():
        count = 0
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("Player 1 Won!\n")
                return True
            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("Player 2 Won!\n")          
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("Its a tie!")
                return True
#This function uses a boolean to see if the game is over after each move. end=true if game is over and false if not.
    while not end:
        displayBoard()
        end = check_board()
        if end == True:
            break
        print("Player 1: Choose a number between 1-9 to place your X")
        player1()
        print()
        displayBoard()
        end = check_board()
        if end == True:
            break
        print("Player 2: Choose a number between 1-9 to place your O")
        player2()
        print()
#Ask players if they would like to play another game or not
    if input("Would you like to play again? (y/n)\n") == "y":
        print()
        TTT()

TTT()