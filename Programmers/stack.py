## 프로세스
from collections import OrderedDict

priorities = [2, 1, 3, 2]
location = 2

pr_dic = OrderedDict((priority, chr(ord('A') + index)) for index, priority in enumerate(priorities))
print(pr_dic)

for i, num in enumerate(priorities):
    print(num)

print("Element at location:", priorities[location])


# priorities의 배열 중 location에 해당하는 값을 따로 저장 = loc
# priorities를 enumerate로 내림차순 정렬
# loc에 저장된 값을 내림차순 정렬한 값과 비교
#출력
