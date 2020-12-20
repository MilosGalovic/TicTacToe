n = "         "
field = [[n[0], n[1], n[2]],
         [n[3], n[4], n[5]],
         [n[6], n[7], n[8]]]
print (f"""
---------
| {field[0][0]} {field[0][1]} {field[0][2]} |
| {field[1][0]} {field[1][1]} {field[1][2]} |
| {field[2][0]} {field[2][1]} {field[2][2]} |
---------""")
x_win = False
o_win = False
counter = 0

while counter <= 8:
    make_move = input("Enter the coordinates: ").split()
    try:
        i = int(make_move[0])
        j = int(make_move[1])
    except ValueError:
        print("You should enter numbers!")
        make_move = input("Enter the coordinates: ").split()
        i = int(make_move[0])
        j = int(make_move[1])

    correct = [1, 2, 3]

    if i not in correct or j not in correct:
        print("Coordinates should be from 1 to 3!")
    else:
        if field[i-1][j-1] not in [" ", "_"]:
            print("This cell is occupied! Choose another one!")
        else:
            if counter % 2 == 0:
                field[i - 1][j - 1] = "X"
            else:
                field[i - 1][j - 1] = "O"
            print(f"""
            ---------
            | {field[0][0]} {field[0][1]} {field[0][2]} |
            | {field[1][0]} {field[1][1]} {field[1][2]} |
            | {field[2][0]} {field[2][1]} {field[2][2]} |
            ---------""")
            counter += 1
            if field[0][0] == field[1][0] == field[2][0] == "X" \
            or field[0][1] == field[1][1] == field[2][1] == "X" \
            or field[0][2] == field[1][2] == field[2][2] == "X" \
            or field[0][0] == field[1][1] == field[2][2] == "X" \
            or field[0][2] == field[1][1] == field[2][0] == "X" \
            or field[0][0] == field[0][1] == field[0][2] == "X" \
            or field[1][0] == field[1][1] == field[1][2] == "X" \
            or field[1][0] == field[1][1] == field[1][2] == "X":
                x_win = True

            if field[0][0] == field[1][0] == field[2][0] == "O" \
            or field[0][1] == field[1][1] == field[2][1] == "O" \
            or field[0][2] == field[1][2] == field[2][2] == "O" \
            or field[0][0] == field[1][1] == field[2][2] == "O" \
            or field[0][2] == field[1][1] == field[2][0] == "O" \
            or field[0][0] == field[0][1] == field[0][2] == "O" \
            or field[1][0] == field[1][1] == field[1][2] == "O" \
            or field[1][0] == field[1][1] == field[1][2] == "O":
                o_win = True

            if x_win is True:
                print("X wins")
                break
            elif o_win is True:
                print("O wins")
                break
            else:
                continue

if x_win == False and o_win == False:
    print("Draw")