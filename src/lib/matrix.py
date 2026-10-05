def transpose(mat: list[list[float | int]]) -> list[list]:
    """Меняет строки и столбцы местами.

    transpose([[1, 2], [3, 4]]) -> [[1, 3], [2, 4]]
    """
    if len(mat) == 0:
        return []
    len_m = len(mat[0])
    m = [[] for _ in range(len_m)]
    for i in range(len(mat)):
        if len(mat[i]) != len_m:
            raise ValueError("Рваная матрица")
        for j in range(len_m):
            m[j].append(mat[i][j])
    return m

# if __name__ == "__main__":
#     print(f"""[[1, 2, 3]] -> {transpose([[1, 2, 3]])}
# [[1], [2], [3]] -> {transpose([[1], [2], [3]])}
# [[1, 2], [3, 4]] -> {transpose([[1, 2], [3, 4]])}
# [] -> {transpose([])}""")
#     print(f"[[1, 2], [3]] -> {transpose([[1, 2], [3]])}")

def row_sums(mat: list[list[float | int]]) -> list[float]:
    """Возвращает сумму по каждой строке. 
    
    row_sums([[1, 2, 3], [4, 5, 6]]) → [6, 15]
    """
    s = []
    len_m = len(mat[0])
    for i in mat:
        if len(i) != len_m:
            raise ValueError("Рваная матрица")
        s.append(sum(i))
    return s

# if __name__ == "__main__":
#     print(f"""[[1, 2, 3], [4, 5, 6]] -> {row_sums([[1, 2, 3], [4, 5, 6]])}
# [[-1, 1], [10, -10]] -> {row_sums([[-1, 1], [10, -10]])}
# [[0, 0], [0, 0]] -> {row_sums([[0, 0], [0, 0]])}""")
#     print(f"[[1, 2], [3]] -> {row_sums([[1, 2], [3]])}")

def col_sums(mat: list[list[float | int]]) -> list[float]:
    """Возвращает сумму по каждому столбцу.
    
    col_sums([[1, 2, 3], [4, 5, 6]] → [5, 7, 9]
    """
    len_m = [len(i) for i in mat]
    if min(len_m) != max(len_m):
        raise ValueError("Рваная матрица")
    s = []
    for i in range(len(mat[0])):
        s.append(sum([mat[j][i] for j in range(len(mat))]))
    return s

# if __name__ == "__main__":
#     print(f"""[[1, 2, 3], [4, 5, 6]] -> {col_sums([[1, 2, 3], [4, 5, 6]])}
# [[-1, 1], [10, -10]] -> {col_sums([[-1, 1], [10, -10]])}
# [[0, 0], [0, 0]] -> {col_sums([[0, 0], [0, 0]])}""")
#     print(f"[[1, 2], [3]] -> {col_sums([[1, 2], [3]])}")