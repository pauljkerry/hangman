def hangman(word):
    wrong = 0 # 間違えた数
    stages = ["",
              "_____________",
              "|",
              "|      |     ",
              "|      0     ",
              "|     /|\    ",
              "|     / \    ",
              "|            "
              ]
    rletters = list(word) #正解のワードを一文字ずつリスト化
    board = ["_"] * len(word) #正解のワード文字数分の空白リスト
    win = False #勝敗判定用で初期は敗北
    print("ハングマンへようこそ！")

    while wrong < len(stages) -1: # 間違えた数がステージ数よりも小さい場合は回り続ける
        print("\n")  #見栄え用
        msg = "1文字を予想してね"
        char = input(msg) #受け取る1文字
        if char in rletters: #正解した場合の分岐
            cind = rletters.index(char) #正解した文字の場所
            board[cind] = char #空白のリストに正解した文字を入れる
            rletters[cind] = "$" #正解のリストに正解した文字を$記号に入れ替える
        else: #間違えた場合の分岐
            wrong += 1 #間違えた数を＋1する
        print(" ".join(board))  #空白のリストの現在の状況を表示
        e = wrong +1 #ステージ数は最終的に間違えた数よりも一つ多くなる
        print("\n".join(stages[0:e])) #間違えたところまでハングマンを表示
        if "_" not in board:
            print("あなたの勝ち!")
            print(" ".join(board)) #埋まったリストを使って正解を表示
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("貴方の負け!正解は{}".format(word))

