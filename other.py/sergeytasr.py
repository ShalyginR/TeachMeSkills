f = 1
p = 1
for _ in range(10):
    print(f)
    f, p = p, p + f

f = 1
p = 1
while f < 1000:
    print(f)
    f, p = p, p + f
