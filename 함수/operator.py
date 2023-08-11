def get_operator(operator):
    if operator == '+':
        return lambda a, b: a + b
    elif operator == '-':
        return lambda a, b: a - b
    elif operator == '*':
        return lambda a, b: a * b
    elif operator == '/':
        return lambda a, b: a / b

# 함수의 반환값으로 람다 함수 사용
add_func = get_operator('+')
result1 = add_func(3, 4)  # 7
print(result1)

multiply_func = get_operator('*')
result2 = multiply_func(3, 4)  # 12
print(result2)
