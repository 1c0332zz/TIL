import random

class Lotto: 
    name = '로또추첨기'

    def generate_lotto(self):
        self.numbers = sorted(random.sample(range(1, 46), 6))

    def get_money(self, real_numbers):
        print('당신의 숫자는', self.numbers)
        print('당첨 숫자는', real_numbers)
        if self.numbers == real_numbers:
            return 10000000000
        else:
            return 0
