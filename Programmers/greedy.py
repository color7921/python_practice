# from itertools import permutations
# def solution(numbers):
#     a = set()
#     for i in range(len(numbers)):
#         a |= set(map(int, map("".join, permutations(list(numbers), i + 1))))
#         print(a)
#     a -= set(range(0, 2))
#     print("0,1 제외한 값",a)
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#         print(a)
#     return len(a)
# result = solution("17")
# print(result)

# from itertools import permutations

# def solution(numbers):
#     a = set()
#     for i in range(len(numbers)):
#         a |= set(map(int, map("".join, permutations(list(numbers), i + 1))))
#         print(f"After permutation {i + 1}: {a}")

#     a -= set(range(0, 2))
#     print(f"After removing 0 and 1: {a}")

#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#         print("a의 값 :", int(max(a) ** 0.5) + 1)
#         print(f"After removing multiples of {i}: {a}")

#     return len(a)

# result = solution("17")
# print(f"Final result: {result}")

# 카펫
# brown = 10
# yellow = 2
# def solution(brown, yellow):
#     total = brown + yellow
#     for i in range(1, total+1):
#         if (total/i)%1 == 0:
#             j = total//i
#             if j >= i:
#                 if 2*i + 2*j == brown+4:
#                     return[j, i]
# result = solution(10, 2)
# print(result)

## 피로도
# from itertools import permutations

# def solution(k, dungeons):
#     answer = 0
    
#     for p in permutations(dungeons, len(dungeons)):
#         tmp = k
#         cnt = 0 
        
#         for need, spend in p:
#             if tmp >= need:
#                 tmp -= spend
#                 cnt += 1
#         answer = max(answer, cnt)
#     return answer
# result = solution(80, [[80,20],[50,40],[30,10]])


## 전력망을 둘로 나누기

# n = 9
# wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]

# def solution(n, wires):
    
#     return 

s = "-1 2 3 4"
a = list(map(int, s.split(" ")))

print(str(max(a)) + " " + str(min(a)))
