# ЛР2 — Коллекции и матрицы (list/tuple/set/dict)
## Задани A
### min_max
```py
def min_max(nums:list[float | int]) -> tuple[float | int, float | int]:
    """Возвращает минимальное и максимальное число в списке.
    
    min_max([7, -1, 2.5, 0, 11]) -> (-1, 11)
    """
    min_n, max_n = nums[0], nums[0]
    if len(nums) == 0:
        raise ValueError("Список пустой")
    for i in nums:
        if i < min_n:
            min_n = i
        if i > max_n:
            max_n = i
    return min_n, max_n
```
![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab02/exA1.png)