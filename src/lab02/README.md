# ЛР2 — Коллекции и матрицы (list/tuple/set/dict)

## Задание 1 — arrays.py

### min_max
Возвращает минимальное и максимальное число в списке. Если список пуст, выдает ошибку ValueError.
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

### unique_sorted
Возвращает отсортированный список уникальных значений. 
```py
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
```
![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab02/exA2.png)

### flatten
«Расплющивает» список списков/кортежей в один список по строкам (row-major). Если встретилась строка/элемент, который не является списком/кортежем выдает ошибку TypeError.
```py
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
```
![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab02/exA3.png)