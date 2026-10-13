# ЛР3 — Тексты и частоты слов (словарь/множество)

## Задание A — src/lib/text.py

### normalize
Нормализует текст. Заменяет ё на е. Заменяет управляющие символы \t, \r, \n на пробел. «Схлопывает» последовательности пробелов в один и обрезает края (strip).
```py
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """нормализует текст.

    "ёжик,      Ёлка   " -> "ежик, елка"
    """
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()
    if yo2e:
        text = text.replace("ё", "е")
    text = text.replace('\r', ' ').replace('\t', ' ')
    text = ' '.join(text.split())
    return text
```
![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab03/exA1.png)


### tokenize
Токенизация. Множество слов — это все подстроки, удовлетворяющие шаблону \\w+(?:-\\w+)*
(буквы/цифры/подчёркивание; допускается дефис внутри слова), разделённые любыми не-\\w символами.
```py
def tokenize(text: str) -> list[str]:
    """Токенизация. Множество слов — это все подстроки, удовлетворяющие шаблону \\w+(?:-\\w+)*
    (буквы/цифры/подчёркивание; допускается дефис внутри слова), разделённые любыми не-\\w символами.

    "2025 год" -> ["2025", "год"]
    """
    l = re.findall(r"\w+(?:-\w+)*", text)
    return l
```
![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab03/exA2.png)


### count_freq
Подсчитывает частоты, возвращает словарь слово → количество.
```py
def count_freq(tokens: list[str]) -> dict[str, int]:
    """Возвращает словарь с количеством слов.

    ["a","b","a","c","b","a"] → {"a":3,"b":2,"c":1}
    """
    s = {}
    for w in tokens:
        s[w] = s.get(w, 0) + 1
    return s
```
![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab03/exA3.png)


### top_n
Возвращает топ-N по убыванию частоты; при равенстве — по алфавиту слова.
```py
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Возвращает топ-N по убыванию частоты; при равенстве — по алфавиту слова.

    top_n(..., n=2) → [("a",3), ("b",2)]
    """
    r = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))[:n]
    return r
```
![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab03/exA4.png)


## Задание B — src/text_stats.py (скрипт со stdin)
Скрипт читает одну строку текста из stdin (или весь ввод до EOF — на ваш выбор, опишите в README), вызывает функции из lib/text.py и печатает:

Всего слов: N
Уникальных слов: K
Топ-5: — по строке на запись в формате слово:кол-во (по убыванию, как в top_n).
```py
from src.lib.text import normalize, tokenize, count_freq, top_n

s = input()

n=normalize(s)
t=tokenize(n)
words=count_freq(t)
top=top_n(words)

print(f"Всего слов: {len(t)}")
print(f"Уникальных слов: {len(words)}")
print(f"Топ-5:")
for x in top:
    print(f"{x[0]}:{x[1]}")
```
![че-то случилося приключилося](https://github.com/wtquu/python_labs/blob/main/images/lab03/exB1.png)