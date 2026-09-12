s = input("in: ")
for i in range(0, len(s)):
    if s[i].isupper():
        i1 = i
        break
n = ''
s = s[i1:]
for i in range(0, len(s)):
    if n.isdigit():
        i2 = i
        break
    n = s[i]
print(f'out: {s[::i2]}')