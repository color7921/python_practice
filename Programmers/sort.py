arr = [6, 2, 10]

answers = ''

arr = list(map(str, arr))
arr.sort(key = lambda x : x*3,reverse=True)

for i in arr:
    answers += i
print(str(int(answers)))