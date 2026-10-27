import csv
from pathlib import Path
from openpyxl import Workbook


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


csv_to_xlsx("data\lab05\samples\cities.csv","data\lab05\out\cities.xlsx")