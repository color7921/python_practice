n = int(input("[3의 배수와 5의 배수 합 구하기]\n\n 양의 정수 n을 입력하세요."))

sum = 0

for i in range(1, n+1):
    if i%3 == 0 or i%5 == 0:
        sum += i
print(f'1부터 {n}까지의 3의 배수와 5의 배수의 총합은 {sum}입니다. ')
