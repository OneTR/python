row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

treasure_map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put your treasure? ")

position_row = int(position) // 10
position_column = int(position) % 10

for row in range(1, 4):
    for column in range(1, 4):
        if position_column == column and position_row == row:
            treasure_map[row - 1][column - 1] = "X"
        if position_row == column and position_column == row:
            treasure_map[column - 1][row - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")