def update(num=0,user=""):
    color = '\033[31m'
    reset_color = '\033[39m'

    if user == "O":
        color = '\033[0;36m'

    for p in range(1,10):
        if num == p:
            positions[p] = color + user + reset_color

    ui = (f"\n {positions[1]} | {positions[2]} | {positions[3]} \n"
          "-----------\n"
          f" {positions[4]} | {positions[5]} | {positions[6]} \n"
          "-----------\n"
          f" {positions[7]} | {positions[8]} | {positions[9]} \n")
    return ui

def check_win(board,player):
    winning_conditions = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [1,4,7],
        [2,5,8],
        [3,6,9],
        [1,5,9],
        [3,5,7]
    ]
    for condition in winning_conditions:
        if all(board[num] == player for num in condition):
            print(f"Player {player} win!!!")
            return True
    return False

positions = ['0','1','2','3','4','5','6','7','8','9']
print(update())

users = ['X','O']
color_users = ['\033[31mX\033[39m','\x1b[0;36mO\x1b[39m']
end_game = False
while not end_game:
    for i in range(2):
        try:
            position = int(input(f"User {color_users[i]} input the position you want: "))
            if position > 9:
                raise ValueError("Please Input a Number From 1 to 9.")
            print(update(position,user=users[i]))
            if check_win(board=positions,player=color_users[i]):
                end_game = True
                break
        except ValueError:
            print(f"Error: Please input a number from 1 to 9.")