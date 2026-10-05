# ЛР2 — Коллекции и матрицы (list/tuple/set/dict)

## Задание 1 — arrays.py

### min_max
Возвращает минимальное и максимальное число в списке. Если список пуст, выдает ошибку.
```py
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
```
![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab02/exA1.png)