# ЛР4 — Файлы: TXT/CSV и отчёты по текстовой статистике

## Задание A — модуль src/lab04/io_txt_csv.py

### read_text
Открывает файл на чтение в указанной кодировке и возвращает содержимое как одну строку. Если файл не найден — поднимает FileNotFoundError,
если кодировка не подходит — поднимает UnicodeDecodeError.
```py
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Возвращает содержимое файла одной строкой.

    По умолчанию кодировка UTF-8.
    Чтобы выбрать другую кодировку, надо добавить второй параметр кодировки, пример: read_text("text.txt", encoding="cp1251")

    Ошибки:
    FileNotFoundError - файл не найден.
    UnicodeDecodeError - не подходящая кодировка.
    """
    p = Path(path)
    return p.read_text(encoding=encoding)
```
Если файл не пустой, возвращает все прочитаное:
![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab04/exA1.png)

Если файл пустой, возвращает пустую строку:
![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab04/exA2.png)

#### Примечание: Считывание целиком позволяет учебное ТЗ. В реальных проектах большие файлы, следует читать построчно из за переполнения памяти.


### write_csv
Создает/перезаписывает CSV с разделителем ",". Если передан header, записывает его первой строкой. Проверяет, что каждая строка в rows имеет одинаковую длину (иначе ValueError).
```py
def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """Создает/перезаписывает CSV с разделителем ",".
    Если передан header, записывает его первой строкой.
    
    Ошибки:
    ValueError - строки в rows не имеют одинаковую длину.
    """
    if len(rows) > 0:
        for row in rows:
            if len(row) != len(rows[0]):
                raise ValueError("Строки разной длины.")
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
```
![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab04/exA3.png)

## Задание B — скрипт src/lab04/text_report.py

### text_report
Читает один входной файл data/input.txt. Нормализует текст (lib/text.py), токенизирует и считает частоты слов. Сохраняет data/report.csv c колонками: word,count, отсортированными: count ↓, слово ↑ (при равенстве). В консоль печатает краткое резюме:
Всего слов: <N>
Уникальных слов: <K>
Топ-5: (список из top_n из ЛР3)
```py
from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv
import sys

try:
    text = read_text('data/lab04/input.txt')
except FileNotFoundError:
    print('Файл не найден.')
    sys.exit(1)
except UnicodeDecodeError:
    print("Неверная кодировка.")
    sys.exit(1)

norm = normalize(text)
t = tokenize(norm)
freq = count_freq(t)
top = top_n(freq, 5)

s = sorted(freq.items(),key=lambda x: (-x[1],x[0]))
write_csv(s,"data/lab04/report.csv", header=("word", "count"))

print(f"""Всего слов: {len(t)}
Уникальных слов: {len(freq)}
Топ-5:""")
for word, count in top:
    print(f"{word}:{count}")
```
![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab04/exB1.png)
![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab04/exB2.png)