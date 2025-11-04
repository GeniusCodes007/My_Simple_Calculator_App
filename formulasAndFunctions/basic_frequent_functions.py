class BasicFrequentFunctions:
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
    #done
    @staticmethod
    def square(num: float): return num ** 2
    #done
    @staticmethod
    def cube(num: float): return num ** 3
    
    @staticmethod
    def square_root(num: float): return num ** (1/2)
    
    def cube_root(self,num: float): return num ** (1/3)
    #done
    @staticmethod
    def percentage(base_num: float, percent_num: float): return float(base_num) * float(percent_num / 100)
    
    @staticmethod
    def recip(num): return float(num) ** (-1)

    #done
    @staticmethod
    def raise_to_power(base_num, expo):
        try:
            if "Result Is Too Large":
                result = base_num ** expo
                return result
        except OverflowError:
            return "Result Is Too Large"
