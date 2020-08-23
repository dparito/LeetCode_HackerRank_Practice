from typing import List

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))


if __name__ == "__main__":
    my_sol = Solution()

    mountain = [0, 1, 2, 1, 0]
    mountain = [0, 2, 1, 0]

    print(my_sol.peakIndexInMountainArray(mountain))
