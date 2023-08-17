import unittest

from src.greedy import (coin_split, 
                        law_of_large_numbers, 
                        count_with_three_in_time
                        k_knight)


class TestGreedy(unittest.TestCase):
    def test_coin_split(self):
        self.assertEqual(coin_split(total_value=1260), 6)
        self.assertEqual(coin_split(total_value=660), 4)

    def test_law_of_large_numbers(self):
        
        answer = law_of_large_numbers((5, 8, 3), (2, 4, 5, 4, 6))
        self.assertEqual(answer, 46)



    def test_count_with_three_in_time(h):
        # 초기값
        count = 0
        # 계산
        for i in range(h+1):
            for j in range(60):
                for k in range(60):
                    if "3" in str(i) + str(j) + str(k):
                        count = count + 1
        #self.assertEqual(count_with_three_in_time(5), 11475)
        # 반환값
        return count

    def test_k_knight(p):
        column = ord(p[0]) - ord('a') + 1
        row = int(p[1])

        steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

        result = 0

        for step in steps:
            next_row = row + step[0]
            next_column = column + step[1]
            if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
                result += 1

        return result




    if __name__ == "__main__":
        pass