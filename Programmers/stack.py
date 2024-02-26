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

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer