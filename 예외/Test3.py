data = {"Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6} 
u = input("입력하세요")
v = data.get(u)

if v is not None:
    print(v)
else:
    print("없는 키")