max_value = 0
min_value = 100
while True:
    num = int(input("1~100의 정수를 입력하세요(종료:0): "))
    if num == 0:
        break
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

print("가장 큰 값: ", max_value)
print("가장 작은 값: ", min_value)