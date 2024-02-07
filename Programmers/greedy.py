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

from itertools import permutations

def solution(numbers):
    a = set()
    for i in range(len(numbers)):
        a |= set(map(int, map("".join, permutations(list(numbers), i + 1))))
        print(f"After permutation {i + 1}: {a}")

    a -= set(range(0, 2))
    print(f"After removing 0 and 1: {a}")

    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
        print("a의 값 :", int(max(a) ** 0.5) + 1)
        print(f"After removing multiples of {i}: {a}")

    return len(a)

result = solution("17")
print(f"Final result: {result}")