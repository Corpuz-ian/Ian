n = 5

for i in range(1, n + 1, 2):
    print(''*((n - i)// 2) + '*' * i)
for i in range(n, 0, -2):
 print('' * ((n - i) // 2) + '*' * i)