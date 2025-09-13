theBoard = {
    #Each tile of the board
    '7': ' ', '8': ' ', '9': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '1': ' ', "2": ' ', '3': ' '
}

#Recording the keys to be able to reset at the end
boardKeys = []
for key in theBoard:
    boardKeys.append(key)
#prints the board
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
#let the games begin
def game():
    #x starts first
    turn = 'X'
    count = 0
    # max of 9 possible moves, start from 0 --> range of 10
    for i in range(10):
        printBoard(theBoard)
        print(f"It's {turn}'s move. Where will you go? ")
        location = input()
        #checks to make sure that the move is possible
        if theBoard[location] == ' ':
            theBoard[location] = turn
            count += 1
        else:
            print("try again, that spot is full")
            continue
        #starts checking for wins from the earliest possible chance
        if count >= 5:
            #the horizontal wins
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("GAME OVER")
                print(f"***** The winner is {turn} *****")
                break
            if theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print("GAME OVER")
                print(f"***** The winner is {turn} *****")
                break
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("GAME OVER")
                print(f"***** The winner is {turn} *****")
                break
            # the vertical wins
            if theBoard['7'] == theBoard['4'] == theBoard['1'] != ' ':
                printBoard(theBoard)
                print("GAME OVER")
                print(f"***** The winner is {turn} *****")
                break
            if theBoard['5'] == theBoard['8'] == theBoard['2'] != ' ':
                printBoard(theBoard)
                print("GAME OVER")
                print(f"***** The winner is {turn} *****")
                break
            if theBoard['6'] == theBoard['3'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("GAME OVER")
                print(f"***** The winner is {turn} *****")
                break
            # diagonal wins
            if theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("GAME OVER")
                print(f"***** The winner is {turn} *****")
                break
            if theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("GAME OVER")
                print(f"***** The winner is {turn} *****")
                break
        # if there are no wins when count is 9, the game ends in tie
        if count == 9:
            print("TIE")
            break
        # changes the turn order to the other person after each person makes a move
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    # after game has ended, the game asks for a repeat and then resets the board
    repeat = input("Try Again? ").lower()
    if repeat == "y" or repeat == "yes":
        for key in boardKeys:
            theBoard[key] = " "
        game()
    else:
        exit()

if __name__ == "__main__":
    print("TIC TAC TOE")
    print()
    game()