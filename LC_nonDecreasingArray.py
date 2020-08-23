from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """
        to check possibility of modifying given int array
        into a non-decreasing array with just 1 change
        input: integer array
        returns: bool
        """

        mod_index = None

        if len(nums) <= 2:
            return True
        elif nums == sorted(nums, reverse=True):
            return False
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if mod_index is not None:
                    return False
                mod_index = i
        
        return (mod_index is None or mod_index == 0 or mod_index == len(nums)-2 or
                nums[mod_index-1] <= nums[mod_index+1] or nums[mod_index] <= nums[mod_index+2])


if __name__ == "__main__":
    my_sol = Solution()

    nums = [3, 4, 2, 3]
    # nums = [4, 2, 1]
    # nums = [1, 2, 3]

    print(my_sol.checkPossibility(nums))
