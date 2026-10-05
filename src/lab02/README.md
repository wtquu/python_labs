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



## Задание B — matrix.py

### transpose
Меняет строки и столбцы местами. Если матрица "рваная", выдает ошибку ValueError.
```py
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
```
![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab02/exB1.png)

### row_sums
Возвращает сумму по каждой строке. Если матрица "рваная", выдает ошибку ValueError.
```py
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
```
![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab02/exB2.png)

### col_sums
Возвращает сумму по каждому столбцу. Если матрица "рваная", выдает ошибку ValueError.
```py
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
```
![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab02/exB3.png)



## Задание C — tuples.py

### format_record
Возвращает фамилию, инициалы, группу и GPA. Если тип данных не подходящий, выдает ошибку TypeError. Если данные некоректные, выдает ошибку ValueError.
```py
def format_record(rec: tuple[str, str, float]) -> str:
    """Возвращает фамилию, инициалы, группу и GPA.
    
    format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)) -> "Иванов И.И., гр. BIVT-25, GPA 4.60"
    Неверный тип данных -> TypeError
    Неверные данные -> ValueError
    """
    if not isinstance(rec, tuple):
        raise TypeError("Не кортеж.")
    if len(rec) != 3:
        raise ValueError("Не хватает данных.")
    if rec[0] == "" or rec[1] == "" or rec[2] == 0:
        raise ValueError("ФИО, группа и GPA не могут быть пустыми.")
    if not isinstance(rec[0], str) or not isinstance(rec[1], str) or not isinstance(rec[2], float):
        raise TypeError("Неверный тип данных.")
    fio = rec[0].split()
    if len(fio) < 2 or 3 < len(fio):
        raise ValueError("ФИО должно состоять из 2 или 3 слов.")
    if rec[2] < 0 or 5 < rec[2]:
        raise ValueError("GPA должен быть в диапазоне от 0 до 5.")

    return f"{fio[0].capitalize()} {fio[1][0].upper()}.{fio[2][0].upper()+'.' if len(fio) == 3 else ''}, гр. {rec[1]}, GPA {rec[2]:.2f}"
```
![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab02/exC1.png)