import random
# 畫棋盤的函式，傳入一個放置棋子的列表
def drawBoard(board) :

    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("------------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("------------")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])

# 玩家選擇所想用的棋子種類
def inputPlayerLetter() :

    letter = ''
    while not (letter == 'X' or letter == 'O') :
        print("Do you want to be X or O")
        # 自動將小寫轉化為大寫
        letter = input().upper()

    # 如果玩家選擇的X，則自動將O賦給電腦，反之一樣
    if letter == 'X' :
        return ['X','O']
    else :
        return ['O','X']

# 這裡隨機生成0或者1來表示誰先落子
def whoGoesFirst() :

    if random.randint(0,1) == 0 :
        return 'computer'
    else :
        return 'player'

# 如果玩家選擇y或者Y則遊戲重新開始
def playAgain():

    print("Do you want to play again?(yes or no)")
    return input().lower().startswith('y')

# 將棋子放置到棋盤上面
# board引數是儲存棋子的列表
# letter引數是棋子的型別
# move是選擇將棋子放在哪
def makeMove(board, letter, move) :

    board[move] = letter

#  根據井字棋規則判斷是否獲勝
def isWinner(bo, le) :

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))

# 將已經在棋盤上的棋子備份,隨時更新
def getBoardCopy(board) :

    dupeBoard = []
    for i in board :
        dupeBoard.append(i)

    return dupeBoard

# 判斷棋盤是否還有可落子的地方
def isSpaceFree(board, move) :

    return board[move] == ' '

# 獲取玩家落子的位置
def getPlayerMove(board) :

    move = ' '
    # 判斷落子的位置是否正確以及棋盤是否還能落子
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)) :

        print("What is your next move?(1-9)")
        move = input()
    return int(move)

# 找到可以落子的地方，主要是計算機使用的
def chooseRandomMoveFromList(board, moveList) :

    possibleMoves = []
    for i in moveList :
        if isSpaceFree(board, i) :
            possibleMoves.append(i)

    if len(possibleMoves) != 0 :
        return random.choice(possibleMoves)
    else :
        return None



# 電腦落子
def getComputerMove(board, computerLetter) :

    # 給出棋盤上電腦和玩家棋子的型別
    if computerLetter == 'X' :
        playerLetter = 'O'
    else :
        playerLetter = 'X'

    for i in range(1,10) :
        # 在備份的棋盤中判斷是否有可以落子的地方
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i) :
            # 如果有可以落子的地方,則先在備份的棋盤上落子
            makeMove(copy, computerLetter, i)
            # 落子後判斷電腦是否能贏,並且返回能贏的落子的位置
            if isWinner(copy, computerLetter) :
                return i

    for i in range(1,10) :
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i) :
            # 在備份的棋盤上模擬玩家落子
            makeMove(copy, playerLetter, i)
            # 如果下一次玩家落子就可以贏,返回玩家落子的位置,用於堵住玩家
            if isWinner(copy, playerLetter) :
                return i

    # 隨機在四個角處落子
    move = chooseRandomMoveFromList(board,[1,3,7,9])
    if move != None :
        return move

    # 如果角處已被佔滿,則落子在中間位置5處
    if isSpaceFree(board, 5) :
        return 5

    # 如果角和中間都被佔滿,則隨機選擇邊上落子
    return chooseRandomMoveFromList(board,[2,4,6,8])

# 判斷棋盤是否已滿
def isBoardFull(board) :

    for i in range(1,10) :
        if isSpaceFree(board, i) :
            return False
    return True


print("Welcome to Tictactoe !!!")

while True :

    # 初始化棋盤為空
    theBoard = [' '] * 10
    # 玩家和電腦棋子型別的選擇
    playerLetter, computerLetter = inputPlayerLetter()
    # 先後順序的決定
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first')
    # 遊戲開始的標誌位,當遊戲結束時變成False
    gameIsPlaying = True

    while gameIsPlaying :
        # 玩家先行
        if turn == 'player' :
            drawBoard(theBoard)
            # 獲取玩家下棋的位置
            move = getPlayerMove(theBoard)
            # 將玩家的棋子傳入列表相應的位置
            makeMove(theBoard, playerLetter, move)

            # 如果玩家獲勝,標誌位變為False
            if isWinner(theBoard, playerLetter) :
                drawBoard(theBoard)
                print("You win !")
                gameIsPlaying = False
            # 否則則判斷棋盤是否已滿
            else :
                if isBoardFull(theBoard) :
                    drawBoard(theBoard)
                    print("Tie")
                    break
                # 若棋盤未滿,且玩家已落子,則下一次落到計算機落子
                else :
                    turn = 'computer'
        # 電腦先行
        else :
            # 電腦隨機選擇位置落子
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            # 如果電腦落子獲勝,則遊戲結束
            if isWinner(theBoard, computerLetter) :
                drawBoard(theBoard)
                print("You lose !")
                gameIsPlaying = False
            else :
                if isBoardFull(theBoard) :
                    drawBoard(theBoard)
                    print("Tie")
                    break
                else :
                    turn = 'player'

    # 玩家沒有再次開始遊戲,則跳出迴圈
    if not playAgain():
        break
