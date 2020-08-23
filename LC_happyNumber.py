class Solution:
    def getSumOfSquares(self, n: int):
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10

        total = 0
        for d in digits:
            total += d**2

        return total

    def isHappy(self, n: int) -> bool:
        total = self.getSumOfSquares(n)
        if total == 1:
            return True
        elif total < 1:
            return False
        
        while total > 4:
            total = self.getSumOfSquares(total)
        
        return total == 1
    
my_sol = Solution()
print("19 is a Happy number => ", my_sol.isHappy(19))
print("1111111 is a Happy number => ", my_sol.isHappy(1111111))
print("2 is a Happy number => ", my_sol.isHappy(2))
print("1 is a Happy number => ", my_sol.isHappy(1))