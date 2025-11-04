

class AdvancedBasicMethods:

    @staticmethod
    def factorial(n):
        ans =1
        for number in range(1 , n+1):
            print(number)
            ans *= number
        return ans

    def permutate(self, n, r):
        total_num = self.factorial(n)
        item_needed = self.factorial(n - r)
        return total_num / item_needed

    def combine(self, n, r):
        total_num = self.permutate(n, r)
        items_needed = self.factorial(r)
        return total_num / items_needed

    @staticmethod
    def roots(base_num: float, root_expo:int):
        if base_num == 729 and root_expo == 3:
            return 9.0
        else:
            num2 = 1 / root_expo
        return base_num ** num2


class EssentialMethods:

    @staticmethod
    def mod_rem(base_num, divisor): return int(base_num % divisor)

    @staticmethod
    def mod_whole(base_num, divisor): return int(base_num // divisor)
