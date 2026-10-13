import re
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

# if __name__ == "__main__":
#     print(f'''"ПрИвЕт\\nМИр\\t" -> "{normalize("ПрИвЕт\nМИр\t")}"
# "ёжик, Ёлка" -> "{normalize("ёжик, Ёлка")}"
# "Hello\\r\\nWorld" -> "{normalize("Hello\r\nWorld")}"
# "  двойные   пробелы  " -> "{normalize("  двойные   пробелы  ")}"''')

def tokenize(text: str) -> list[str]:
    """Токенизация. Множество слов — это все подстроки, удовлетворяющие шаблону \\w+(?:-\\w+)*
    (буквы/цифры/подчёркивание; допускается дефис внутри слова), разделённые любыми не-\\w символами.

    "2025 год" -> ["2025", "год"]
    """
    l = re.findall(r"\w+(?:-\w+)*", text)
    return l

# if __name__ == "__main__":
#     print(f'''"привет мир" -> {tokenize("привет мир")}
# "hello,world!!!" -> {tokenize("hello,world!!!")}
# "по-настоящему круто" -> {tokenize("по-настоящему круто")}
# "2025 год" -> {tokenize("2025 год")}
# "emoji 😀 не слово" -> {tokenize("emoji 😀 не слово")}''')


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Возвращает словарь с количеством слов.

    ["a","b","a","c","b","a"] → {"a":3,"b":2,"c":1}
    """
    s = {}
    for w in tokens:
        s[w] = s.get(w, 0) + 1
    return s

# if __name__ == "__main__":
#     print(f'''["a","b","a","c","b","a"] -> {count_freq(["a","b","a","c","b","a"])}
# ["bb","aa","bb","aa","cc"] -> {count_freq(["bb","aa","bb","aa","cc"])}''')


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Возвращает топ-N по убыванию частоты; при равенстве — по алфавиту слова.

    top_n(..., n=2) → [("a",3), ("b",2)]
    """
    r = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))[:n]
    return r

if __name__ == "__main__":
    print('top_n({"a":3,"b":2,"c":1}, 2) -> '+f'{top_n({"a":3,"b":2,"c":1}, 2)}')
    print('top_n({"aa":2,"bb":2,"cc":1}, 2) -> '+f'{top_n({"aa":2,"bb":2,"cc":1}, 2)}')