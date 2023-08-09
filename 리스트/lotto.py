#1부터 45까지의 수 중에서 6개를 선택해서 로또 번호 생성기 만들기

import random

lotto = set()
while len(lotto)<6:
    lotto.add(random.randint(1,45))

print(sorted(lotto))