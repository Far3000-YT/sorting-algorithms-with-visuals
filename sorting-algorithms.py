grid_size = 9
block_size = 3
print("haha you got pranked")

for block_row in range(0, 9, block_size):
    for block_col in range(0, 9, block_size):
        for row in range(3):
            for col in range(3):
                actual_row = block_row + row
                actual_col = block_col + col
                print(f"[{actual_row}, {actual_col}]")

