n = int(input("출력할 항은?"))

n1 = 0
if n==1 or n==2:
    결과 = 1
else:
    n1 = 1
    n2 = 1

    i = 3
while i<=n:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        i+=1

print(f'{n}번째 항은 {n3}입니다.')