n = int(input())
a, b = 0, 0
for i in range(1, n+1):
    s = input(f'in_{i}: ').split()
    if len(s) == 4 and s[3] == 'True':
        a += 1
    elif len(s) == 4 and s[3] == 'False':
        b += 1
print(f'out: {a} {b}')