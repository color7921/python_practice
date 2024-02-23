## JadenCase 문자열 만들기

# s = "3people unFollowed me"

# a = s.split()
# b = ''
# for i in range(len(a)):
#     b += a[i][0].upper() + a[i][1::].lower() + " "

## 타겟 넘버
# numbers = [1, 1, 1, 1, 1]
# target = 3

## 최솟값 만들기

# A = [1, 4, 2]
# B = [5, 4, 4]

# A.sort(reverse=True)
# B.sort()
# answer = 0
# for i in range(len(A)):
#     answer += (A[i]*B[i])
# print(answer)

## 올바른 괄호
# s = "()("
# arr = list(s)
# count = 0
# for i in range(len(arr)):
#     if arr[i] == '(':
#         count += 1
#     else :
#         count -= 1
# if count == 0:
#     print(True)
# else :
#     print(False)

s = "()("
count = 0
for i in s:
    if i == '(':
        count += 1
    else:
        if count > 0:
            count -= 1
        else:
            print(False)
if count == 0:
    print(True)
else:
    print(False)