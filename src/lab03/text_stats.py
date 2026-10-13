from src.lib.text import normalize, tokenize, count_freq, top_n

s = input()

n=normalize(s)
t=tokenize(n)
words=count_freq(t)
top=top_n(words)

print(f'''Всего слов: {len(t)}
Уникальных слов: {len(words)}
Топ-5:''')
for x in top:
    print(f"{top[x][0]}:{top[x][1]}")