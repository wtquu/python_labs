import csv
from pathlib import Path
from typing import Iterable, Sequence

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

if __name__ == '__main__':
    print(read_text('data/lab04/input.txt', encoding= 'utf-8'))
    print(write_csv([("word","count"),("test",3)], "data/lab04/check.csv"))