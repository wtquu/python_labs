# ЛР7 — Поиск, сортировка и измерение времени

## Задание A. Поиск (search.py)

### linear_search
Возвращает индекс первого вхождения x или -1, если данного элемента нет.
Сложность: О(n) (один раз проходит список).
```py
def linear_search(nums, x):
    """Индекс первого вхождения x или -1.
 
    linear_search([4, 2, 7, 2], 2) -> 1
    linear_search([4, 2, 7, 2], 9) -> -1
    linear_search([], 1) -> -1
    """
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1
```

### binary_search
Возвращает индекс x в отсортированном по возрастанию списке или -1, если данного элемента нет. На неотсортированном списке результат не определён.
Сложность: О(log n) (на каждом шаге цикла область поиска уменьшается примерно вдвое).
```py
def binary_search(sorted_nums, x):
    """Индекс x в отсортированном по возрастанию списке или -1.
    На неотсортированном списке результат не определён.
 
    binary_search([1, 3, 5, 7], 5) -> 2
    binary_search([1, 3, 5, 7], 4) -> -1
    binary_search([5], 5) -> 0
    binary_search([], 5) -> -1
    """
    lo = 0
    hi = len(sorted_nums)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if sorted_nums[mid] < x:
            lo = mid + 1
        elif x < sorted_nums[mid]:
            hi = mid - 1
        else:
            return mid
    return -1
```

### two_sum_brute
Возвращает пару индексов, значение элементов которых в сумме дают target или None, если таких элементов нет.
Сложность: О(n^2) (цикл в цикле).
```py
def two_sum_brute(nums, target):
    """Пара индексов (i, j), i < j, nums[i] + nums[j] == target, или None.
 
    two_sum_brute([2, 7, 11, 15], 9) -> (0, 1)
    two_sum_brute([1, 2], 10) -> None
    """
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None
```

### two_sum_fast
Возвращает пару индексов, значение элементов которых в сумме дают target или None, если таких элементов нет.
Сложность: О(n) (один проход цикла).
```py
def two_sum_fast(nums, target):
    """То же, что two_sum_brute, но за один проход со словарём."""
    s = {}
    for i in range(len(nums)):
        n = target - nums[i]
        if n in s:
            return (s[n], i)
        s[nums[i]] = i
    return None
```

## Задание B. Сортировки (sorting.py)

### bubble_sort
Сортировка "пузырьком": проходит по списку необходимое количество раз, меняя соседние элементы, если они стоят в неправильном порядке, пока весь список не будет стоять в порядке возрастания.
Сложность: О(n^2) (цикл в цикле) или О(n) (если список сразу отсортирован).
```py
def bubble_sort(nums):
    """Новый список, отсортированный по возрастанию. Исходный не меняется.
 
    bubble_sort([3, 1, 2]) -> [1, 2, 3]
    bubble_sort([2, 2, 1]) -> [1, 2, 2]
    bubble_sort([]) -> []
    """
    nums = list(nums)
    for i in range(len(nums)-1):
        f = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums
```

### insertion_sort
Сортировка вставками: сдвигает элементы, которые больше текущего вправо, и вставляет в подходящее место.
Сложность: О(n^2) (while в цикле) или О(n) (если список сразу отсортирован).
```py
def insertion_sort(nums):
    """Новый список, отсортированный по возрастанию. Исходный не меняется.
    insertion_sort([3, 1, 2]) -> [1, 2, 3]
    insertion_sort([2, 2, 1]) -> [1, 2, 2]
    insertion_sort([]) -> []
    """
    nums = list(nums)
    for i in range(1, len(nums)):
        n = nums[i]
        j = i-1
        while j >= 0 and n < nums[j]:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = n
    return nums
```

### selection_sort
Сортировка выбором: ищет минимальное число хвоста и вставляет его на границу отсортированной части.
Сложность: О(n^2) (внутренний цикл всегда проходит весь остаток, независимо от данных).
```py
def selection_sort(nums):
    """Новый список, отсортированный по возрастанию. Исходный не меняется.
    selection_sort([3, 1, 2]) -> [1, 2, 3]
    selection_sort([2, 2, 1]) -> [1, 2, 2]
    selection_sort([]) -> []
    """
    nums = list(nums)
    for i in range(len(nums)-1):
        min_n = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_n]:
                min_n = j
        nums[i], nums[min_n] = nums[min_n], nums[i]
    return nums
```

## Задание C. Проверка против эталона (check.py)

### check_sorting
Проверяет функцию сортировки на случайных списках: результат должен совпадать с sorted(), а исходный список - не меняться. При несовпадении поднимается AssertionError с указанием проблемного входа.
```py
def check_sorting(fn, trials=100):
    """сравнивает fn(nums) со sorted(nums)"""
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"
```

### check_search
Проверяет функции поиска на случайных списках: результат linear_search должен совпадать с nums.index(), а для binary_search элемент по индексу должен совпадать с x (могут быть повторы, поэтому важно просто наличие элемента). При несовпадении поднимается AssertionError с указанием проблемного входа.
```py
def check_search(trials=100):
    """сравнивает linear_search и binary_search с list.index"""
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        x = random.randint(-150, 150)
        sorted_nums = sorted(nums)
        try:
            expected = nums.index(x)
        except ValueError:
            expected = -1
        assert linear_search(nums, x) == expected, f"linear_search ошиблась на {nums}, x = {x}"
        result_binary = binary_search(sorted_nums, x)
        if result_binary != -1:
            assert  0 <= result_binary < len(sorted_nums), f"индекс вне диапазона {len(sorted_nums)}: функция выдала {result_binary}"
            assert sorted_nums[result_binary] == x, f"binary_search ошиблась на {nums}, x = {x}"
        else:
            assert x not in sorted_nums, f"binary_search не нашла {x} в {sorted_nums}"
    return trials
```

### check_two_sum
Проверяет функции поиска пары чисел на случайных списках: результат должен совпадать с эталоном. При несовпадении поднимается AssertionError с указанием проблемного входа.
```py
def check_two_sum(trials=100):
    """ оба способа должны давать пару с нужной суммой или оба None
    
    при расхождении — AssertionError с данными, на которых разошлось"""
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-50, 50) for _ in range(n)]
        x = random.randint(-200, 200)

        res_brute = two_sum_brute(nums, x)
        res_fast  = two_sum_fast(nums, x)
        expected = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == x:
                    expected.append((i, j))
        if expected:
            assert res_brute in expected, f"two_sum_brute ошибся на {nums}, target = {x}"    
            assert res_fast in expected, f"two_sum_fast ошибся на {nums}, target = {x}"    
        
        else:            
            assert res_brute is None, f"two_sum_brute нашел результат, хотя ожидалось None"
            assert res_fast is None, f"two_sum_fast нашел результат, хотя ожидалось None"
    return trials
```

Запуск проверки:
```py
if __name__ == "__main__":
    random.seed(42)
    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)
    check_search()
    check_two_sum()
    print("OK")
```
![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab07/ex01.png)


## Задание D. Бенчмарк (bench.py)

### bench_sorts
Замеряет время sorted() и трёх написанных сортировок на списках размером 1_000, 10_000 и 100_000 элементов и возвращает результаты списком кортежей. Для 100_000 написанные сортировки не запускает (слишком долго) — пишет ">60".
```py
def bench_sorts():
    random.seed(42)
    rows = []
    for n in (1_000, 10_000, 100_000):
        data = [random.randint(-10**6, 10**6) for _ in range(n)]
        t = timeit.timeit(lambda: sorted(data), number=1)
        rows.append(("sort", n, "sorted", f"{t:.6f}"))

        for func in (bubble_sort, insertion_sort, selection_sort):
            name = func.__name__
            if n <= 10_000:
                t = timeit.timeit(lambda: func(data), number = 1)
                rows.append(("sort", n, name, f"{t:.6f}"))
            else:
                rows.append(("sort", n, name, ">60"))
    return rows
```

### bench_search
Замеряет время функций на 10 000 запросах. Возвращает список кортежей.
```py
def bench_search():
    random.seed(42)
    rows = []
    data = [random.randint(-10**6, 10**6) for _ in range(100_000)]
    targets = [random.choice(data) for _ in range(10000)]
        
    t_lin = timeit.timeit(lambda: [linear_search(data, x) for x in targets], number=1)
    rows.append(("search", 100_000, "linear_search", f"{t_lin:.6f}"))
        
    sorted_data = sorted(data)
    t_bin = timeit.timeit(lambda: [binary_search(sorted_data, x) for x in targets], number=1)
    rows.append(("search", 100_000, "binary_search", f"{t_bin:.6f}"))
    return rows
```

### bench_2sum
Замеряет время функций на 1_000 и 10_000 запросах. Функции получают одни и те же данные. Возвращает список кортежей.
```py
def bench_2sum():
    random.seed(42)
    rows = []
    
    for n in (1_000, 10_000):
        data = [random.randint(-10**6, 10**6) for _ in range(n)]
        a, b = random.sample(data, 2)
        target = a + b

        t_2sb = timeit.timeit(lambda: two_sum_brute(data, target), number=1)
        rows.append(("two_sum", n, "two_sum_brute", f"{t_2sb:.6f}"))

        t_2sf = timeit.timeit(lambda: two_sum_fast(data, target), number=1)
        rows.append(("two_sum", n, "two_sum_fast", f"{t_2sf:.6f}"))
    
    return rows
```

### main
Собирает результаты всех трёх бенчмарков, сохраняет их в CSV и печатает выровненную таблицу в консоль.
```py
def main():
    rows = bench_sorts() + bench_search() + bench_2sum()
    write_csv(rows, "data/lab07/bench.csv", ("задание", "n", "функция", "секунды"))

    max_len = 0
    for func in (bubble_sort, insertion_sort, selection_sort, linear_search, binary_search, two_sum_brute, two_sum_fast):
        name = func.__name__
        max_len = max(max_len, len(name))
    
    print(f"{'задание':<12} | {'n':<8} | {'функция':<{max_len}} | {'секунды':<12}")
    print("-" * (41 + max_len))
    for task, n, func, sec in rows:
        print(f"{task:<12} | {n:<8} | {func:<{max_len}} | {sec:<12}")
```

Запуск:

![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab07/ex02.png)

![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab07/ex03.png)

Вывод:
Время пузырька выросло в 110 раз из-за сложности O(n^2), а sorted - всего в 16 раз, так как сложность O(n log n) растет медленнее.
На неотсортированных данных бинарный поиск не работает (отбрасывает не те половины), поэтому перед поиском массив нужно сортировать.
C помощью check.py обнаружила ошибки в коде сортировок, из-за чего возвращались списки с одинаковыми значениями. Все ошибки были исправлены.