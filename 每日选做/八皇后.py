def eight_queens():
    solutions = []

    def is_safe(row, col):
        for r in range(row):
            if (cols[r] == col or abs(cols[r] - col) == abs(r - row)):
                return False
        return True

    def solve(row):
        if row == 8:
            solutions.append(''.join(str(c + 1) for c in cols))
            return
        for col in range(8):
            if is_safe(row, col):
                cols[row] = col
                solve(row + 1)
                cols[row] = -1  

    cols = [-1] * 8
    solve(0)
    return solutions

queen_solutions = eight_queens()

n = int(input())
for _ in range(n):
    b = int(input())
    print(queen_solutions[b - 1])  