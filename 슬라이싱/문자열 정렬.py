s = "hello worldaaa"
print(len(s))
print(s*10)
print(s[0:1])
print(s[:3])
print(s[:])
print(s[::-1])
if s[7:8]:
    print(s)
else:
    s = str(input("문자가 없습니다."))
print(s.strip())
print(s.upper())
print(s.lower())
print(s.replace("a", "e"))


# 문자 'a'가 들어가는 단어를 키보드에서 입력 받아 첫 번째 줄에는 'a'까지의 문자열을 출력하고 두 번째 줄에는 나머지 문자열을 출력하는 프로그램을 작성하라.

n = 'Buffalo'

print(str(n.index("a")))