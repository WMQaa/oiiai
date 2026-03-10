def solve_n_queens(n):
    solutions = []
    def backtrack(row, cols, diag1, diag2):
        if row == n:
            solutions.append(cols.copy())
            return
        for col in range(n):
            if col not in cols and (row - col) not in diag1 and (row + col) not in diag2:
                cols.append(col)
                diag1.add(row - col)
                diag2.add(row + col)
                backtrack(row + 1, cols, diag1, diag2)
                cols.pop()
                diag1.remove(row - col)
                diag2.remove(row + col)
    backtrack(0, [], set(), set())
    return solutions