# ЛР5 — JSON и конвертации (JSON↔CSV, CSV→XLSX): Техническое задание

## Задание A — JSON ↔ CSV

### json_to_csv
```py
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
    if not all(type(item) != dict for item in data):
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
```
Функция:
1. Проверяет есть ли файл и его расширение.
2. Считывает данные с помощью json.load() и проверяет,что объект является непустым списком словарей.
3. Формирует список столбцов из всех ключей в порядке их первого появления.
4. Записывает заголовок и строки в CSV.

![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab05/exA1.png)

### csv_to_json
```py
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
```
Функция:
1. Проверяет есть ли файл и его расширение.
2. С помощью csv.DictResder(f) первая строка становится ключами(заголовками), остальные строки - словарями.
3. Проверяет наличие содержимого в файле.
4. Полученный список словарей сохраняется с помощью json.dump() с отступом в два пробела.

![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab05/exA2.png)

## Задание B — CSV → XLSX

### csv_to_xlsx
```py
def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    cf=Path(csv_path)
    xf=Path(xlsx_path)

    if not cf.exists():
        raise FileNotFoundError("файл не найден.")
    if cf.suffix.lower() != ".csv":
        raise ValueError("Неверный тип файла. Расширение должно быть .csv.")
    if xf.suffix.lower() != ".xlsx":
        raise ValueError("Неверный тип файла. Расширение должно быть .xlsx.")

    with open(cf, "r", encoding = "utf-8", newline = "") as f:
        reader = list(csv.reader(f))

    if not reader:
        raise ValueError("Файл CSV пустой.") 
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    for row in reader:
        ws.append(row)

    for c in ws.columns:
        max_len = 0
        letter = c[0].column_letter

        for cell in c:
            if cell.value and len(str(cell.value)) > max_len:
                max_len = len(str(cell.value))

        ws.column_dimensions[letter].width = max(max_len, 8)

    wb.save(xf)
```
Функция:
1. Проверяет есть ли файл и его расширение.
2. Читает строки в кодировке UTF-8
3. Создает книгу Excel с помощью openpyxl и добавляет строки CSV в лист Sheet1 с помощью ws.append().
4. Ищет самый длинный текст в колонке и устанавливет ширину столбцов по максимальной длине содержимого.
5. Сохраняет результат по указанному пути.

![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab05/exB.png)