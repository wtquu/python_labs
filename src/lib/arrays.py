def min_max(nums:list[float | int]) -> tuple[float | int, float | int]:
    """Возвращает минимальное и максимальное число в списке.
    
    min_max([7, -1, 2.5, 0, 11]) -> (-1, 11)
    """
    if len(nums) == 0:
        raise ValueError("Список пустой")
    min_n, max_n = nums[0], nums[0]
    for i in nums:
        if i < min_n:
            min_n = i
        if i > max_n:
            max_n = i
    return min_n, max_n


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """Возвращает отсортированный список уникальных значений.

    unique_sorted([0, -5, 8, 1, 10, 8]) -> [-5, 0, 1, 8, 10]
    """
    l = list(set(nums))
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l


def flatten(mat: list[list | tuple]) -> list:
    """«Расплющивает» список списков/кортежей в один список по строкам (row-major).

    flatten([[0, 1, 2], (3, 4)]) -> [0, 1, 2, 3, 4]
    """
    l = list()
    for i in mat:
        if not isinstance(i, (list, tuple)):
            raise TypeError("строка не строка строк матрицы")
        for j in i:
            l.append(j)
    return l


# if __name__ == "__main__":
#     print(f"""[3, -1, 5, 5, 0] -> {min_max([3, -1, 5, 5, 0])}
# [42] -> {min_max([42])}
# [-5, -2, -9] -> {min_max([-5, -2, -9])}
# [1.5, 2, 2.0, -3.1] -> {min_max([1.5, 2, 2.0, -3.1])}""")
#     print(f"[] -> {min_max([])}")

# if __name__ == "__main__":
#     print(f"""[3, 1, 2, 1, 3] -> {unique_sorted([3, 1, 2, 1, 3])}
# [] -> {unique_sorted([])}
# [-1, -1, 0, 2, 2] -> {unique_sorted([-1, -1, 0, 2, 2])}
# [1.0, 1, 2.5, 2.5, 0] -> {unique_sorted([1.0, 1, 2.5, 2.5, 0])}""")

# if __name__ == "__main__":
#     print(f"""[[1, 2], [3, 4]] -> {flatten([[1, 2], [3, 4]])}
# [[1, 2], (3, 4, 5)] -> {flatten([[1, 2], (3, 4, 5)])}
# [[1], [], [2, 3]] -> {flatten([[1], [], [2, 3]])}""")
#     print(f'[[1, 2], "ab"] -> {flatten([[1, 2], "ab"])}')