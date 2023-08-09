def calculate(x,y):
    add = x + y
    subtract = x - y
    multiply = x*y
    divide = x/y
    return add, subtract, multiply, divide

a,b,c,d = calculate(20,30)
print(a,b,c,f'{d:.2f}')

#딕셔너리

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(my_dict['name'])  # 'Alice'
print(my_dict['city'])  


my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
if 'name' in my_dict:
    print(my_dict['name'])  # 'Alice'
if 'phone' in my_dict:
    print(my_dict['age'])  



#딕셔너리 연습문제

#days = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31,'September':30, 'October':31, 'November':30, 'December':31}

#print(sorted(list(days.keys())))

#for x in days.keys():
   # print(f'{x}:{days[x]}')
#days = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30}
#dm = [(d,m) for (m,d) in days.items()]
#sdm = sorted(dm)
#smd = [(m,d) for (d, m) in sdm]

d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},{'name':'Princess', 'phone':'555-3141', 'email':''},{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

for p in d:
    if p['phone'][7] =='8':
        print(p['name'])

print('-'*20)

for p in d:
    if p['email']=='':
        print(p['name'])
n = input("이름:")

for p in d:
    if p['name']==n:
        print(f"전화번호:{p['phone']}\n이메일:{p['email']}")
        flag = 0

if flag == 1:
    print("이름이 없습니다.")