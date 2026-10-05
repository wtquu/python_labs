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


# def flatten(mat: list[list | tuple]) -> list:
#     """
#     """


# if __name__ == "__main__":
#     print(f"""[3, -1, 5, 5, 0] -> {min_max([3, -1, 5, 5, 0])}
# [42] -> {min_max([42])}
# [-5, -2, -9] -> {min_max([-5, -2, -9])}
# [1.5, 2, 2.0, -3.1] -> {min_max([1.5, 2, 2.0, -3.1])}""")
#     print(f"[] -> {min_max([])}")

