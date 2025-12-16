# MathUtils-calculate sum


class MathUtils:

    @staticmethod
    def calculateSum(numbers):
        return sum(numbers)


numbers = [10, 30, 40, 65, 70]
result = MathUtils.calculateSum(numbers)
print("sum of numbers:", result)
