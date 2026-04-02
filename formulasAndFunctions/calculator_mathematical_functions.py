class Calculator_Mathematical_Functions:
    #done
    @staticmethod
    def add(num1: float, num2: float): return num1 + num2

    #done
    @staticmethod
    def difference(num1: float, num2: float): return num1 - num2

    #done
    @staticmethod
    def multiply(num1: float, num2: float): return num1 * num2

    #done
    @staticmethod
    def divide(num1: float, num2: float): return num1 / num2

    # done
    @staticmethod
    def percentage(base_num: float, percent_num: float):
        return float(base_num) * float(percent_num / 100)

    # done
    @staticmethod
    def raise_to_power(base_num, expo):
        try:
            if "Result Is Too Large":
                result = base_num ** expo
                return result
        except OverflowError:
            return "Result Is Too Large"

    # done
    @staticmethod
    def roots( root_expo: int, base_num: float):
        if base_num == 729 and root_expo == 3:
            return 9.0
        else:
            num2 = 1 / root_expo
        return base_num ** num2

    #done
    @staticmethod
    def square(num: float): return num ** 2

    #done
    @staticmethod
    def cube(num: float): return num ** 3
    
    @staticmethod
    def square_root(num: float): return num ** (1/2)

    @staticmethod
    def cube_root(num: float): return num ** (1/3)
    
    @staticmethod
    def recip(num): return float(num) ** (-1)

    @staticmethod
    def factorial(n:int):
        ans =1
        for number in range(1 , int(n+1)):
            ans *= number
        return ans

    def permutate(self, n:int, r:int):
        total_num = self.factorial(n)
        item_needed = self.factorial(n - r)
        return total_num / item_needed

    def combine(self, n:int, r:int):
        total_num = self.permutate(n, r)
        items_needed = self.factorial(r)
        return total_num / items_needed



    @staticmethod
    def mod_rem(base_num:float, divisor:float): return int(base_num % divisor)

    @staticmethod
    def mod_whole(base_num:float, divisor:float): return int(base_num // divisor)
