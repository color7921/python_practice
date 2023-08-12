def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        print("0으로 나눌 수 없습니다.")
    else:
        return x/y
if __name__ == '__main__':
    print(add(4,3))
    print(subtract(4,3))
    print(multiply(4,3))
    print(divide(4,3))

from mymath import *

x = 3
y = 4

print(add(4,3))
print(subtract(4,3))
print(multiply(4,3))
print(divide(4,3))