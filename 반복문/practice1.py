# 플레이어가 처음에 $50을 가지고 있다. 동전을 한 번 던져서 앞면(1) 또는 뒷면(2)이 나온다. 
# 맞추면 $9을 따고 틀리면 $10을 잃는다. 플레이어가 돈을 모두 잃거나 $100이 되면 게임이 종료된다.
# 동전을 던져서 나오는 수는 다음 문장을 이용하라.

import random

p = 50

while True:
    coin = random.randint(1,2)
    guess = int(input("앞/뒤(1/2)?"))

    if coin == guess:
        p += 9
        print(f"승:{p}")
    else:
        p -= 10
        print(f"패:{p}")

    if p>=100 or p<=0:
        break