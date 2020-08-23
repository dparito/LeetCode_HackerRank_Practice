class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        else:
            count = 0
            for x in range(2, n):
                divisible = False
                for i in range(2, x):
                    if x % i == 0:
                        divisible = True
                        break
                if not divisible:
                    count += 1
            return count
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.countPrimes(10))