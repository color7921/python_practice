# 2. 가장 큰 수

# arr = [6, 2, 10]

# answers = ''

# arr = list(map(str, arr))
# arr.sort(key = lambda x : x*3,reverse=True)

# for i in arr:
#     answers += i
# print(str(int(answers)))

# 깨달은 점
# lambda 사용법, 반복문과 문자열의 관계

###################################

# 3. H-Index

citations = [2, 0, 2, 1, 1]

citations.sort(reverse=True)

for i in range(len(citations)):
    if citations[i] < i + 1:
        print(i)
        break
# print(len(citations))
    