def print_solution(n):
    global count
    print(f"\n\nSolution {count}:\n\n", end="")
    for i in range(1, n + 1):
        print(f"\t{i}", end="")
    for i in range(1, n + 1):
        print(f"\n\n{i}ui", end="")
        for j in range(1, n + 1):
            if board[i] == j:
                print("\t",j, end="")
            else:
                print("\t-", end="")
    count += 1
    
def place(row, column):
    for i in range(1, row):
        if board[i] == column or abs(board[i] - column) == abs(i - row):
            return 0
    return 1

def queen(row, n):
    for column in range(1, n + 1):
        if place(row, column):
            board[row] = column
            if row == n:
                print_solution(n)
            else:
                queen(row + 1, n)
                
board = [0] * 20
count = 0
n = int(input("\n\nEnter number of Queens: "))
queen(1, n)
