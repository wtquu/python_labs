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