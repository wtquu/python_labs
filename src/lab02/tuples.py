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

if __name__ == "__main__":
    print(f"""("Иванов Иван Иванович", "BIVT-25", 4.6) -> {format_record(("Иванов Иван Иванович", "BIVT-25", 4.6))}
("Петров Пётр", "IKBO-12", 5.0) -> {format_record(("Петров Пётр", "IKBO-12", 5.0))}
("Петров Пётр Петрович", "IKBO-12", 5.0) -> {format_record(("Петров Пётр Петрович", "IKBO-12", 5.0))}
("  сидорова  анна   сергеевна ", "ABB-01", 3.999) -> {format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))}""")
    print(f'("", "", 4.0) -> {format_record(('', '', 4.0))}')

    

    
    

    