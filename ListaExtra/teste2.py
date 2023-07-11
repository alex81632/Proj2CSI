n = 2**1 * 3**1

count = 1

count = 0

for i in range(2):
    for j in range(2):
        num = (2**i * 3**j)
        print(num)
        if n**2 %num == 0 and n%num != 0 and num < n:
            count += 1
            print(i, j, num)
            

print(count)