from pathlib import Path
import csv
import json

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    jf = Path(json_path)
    cf = Path(csv_path)

    if not jf.exists():
        raise FileNotFoundError("Файл не найден.")
    if jf.suffix.lower() != ".json":
        raise ValueError("Неверный тип файла. Расширение должно быть .json.")
    if cf.suffix.lower() != ".csv":
            raise ValueError("Неверный тип файла. Расширение должно быть .csv.")

    with jf.open('r',encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Невереный формат JSON или файл пуст.")

    if len(data) == 0:
        raise ValueError("Пустой JSON файл.")
    if type(data) != list:
        raise ValueError("Невереный тип данных.")
    if not all(type(item) == dict for item in data):
        raise ValueError("JSON должен содержать список словарей.")

    l=[]
    for item in data:
        for key in item:
            if key not in l:
                l.append(key)
    
    with cf.open('w', newline="" ,encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=l)
        w.writeheader()
        w.writerows(data)

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    jf = Path(json_path)
    cf = Path(csv_path)
    
    if not cf.exists():
        raise FileNotFoundError("Файл не найден.")
    if cf.suffix.lower() != ".csv":
        raise ValueError("Неверный тип файла. Расширение должно быть .csv.")
    if jf.suffix.lower() != ".json":
        raise ValueError("Неверный тип файла. Расширение должно быть .json.")
    
    with cf.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("Файл CSV пустой.")
        data = list(reader)
    
    if len(data)==0:
        raise ValueError('Файл CSV не содержит данных')
    with jf.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii = False, indent = 2)


# json_to_csv("data\lab05\samples\people.json","data\lab05\out\people_from_json.csv")
# csv_to_json("data\lab05\samples\people.csv","data\lab05\out\people_from_csv.json")