
from formulasAndFunctions.advanced_basic_methods import EssentialMethods
import math
class TrigMethods(EssentialMethods):
    def sine(self, angle:float):
        if self.mod_rem(angle, 360) == 30:
            return (1/2)

        elif self.mod_rem(angle, 360) == 0:
            return 0.0

        elif self.mod_rem(angle, 360) == 90:
            return 1.0

        elif self.mod_rem(angle, 360) == 180:
            return 0.0

        elif self.mod_rem(angle, 360) == 270:
            return -1.0

        else:
            sine_ = math.sin(math.pi * (angle / 180))
            return sine_

    def cos(self, angle: float):
        if self.mod_rem(angle, 360) == 0:
            return 1.0

        elif self.mod_rem(angle, 360) == 60:
            return 0.5

        elif self.mod_rem(angle, 360) == 90:
            return 0.0

        elif self.mod_rem(angle, 360) == 180:
            return -1.0

        elif self.mod_rem(angle, 360) == 270:
            return 0.0

        else:
            cos_ = math.cos(math.pi * (angle / 180))
            return float(cos_)

    def tan(self, angle:float):
        try:
            sin = self.sine(angle)
            cosine = self.cos(angle)
            tan = sin / cosine
            return tan
        except ZeroDivisionError:
            return "For " + str(angle) + " The Result Is Undefined, " + "\nDivision By Zero Is Infinite"


class Inverse:

    @staticmethod
    def arc_sine(num: float):
        try:
            result = math.asin(num)
            result_in_degrees = math.degrees(result)
            return result_in_degrees
        except ValueError:
            return f"Number: {num},Out of Range"

    @staticmethod
    def arc_cosine(num: float):
        try:
            result = math.acos(num)
            result_in_degrees = math.degrees(result)
            return result_in_degrees
        except ValueError:
            return f"Number: {num},Out of Range"

    @staticmethod
    def arc_tangent(num: float):
        try:
            result = math.atan(num)
            result_in_degrees = math.degrees(result)
            return result_in_degrees
        except ValueError:
            return f"Number: {num},Out of Range"
