from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        nums_set = set(nums)
        return [i for i in range(1,len(nums)+1) if i not in nums_set]        
        

if __name__ == "__main__":
    my_sol = Solution()

    my_num_arr = [4,3,2,7,8,2,3,1]
    my_num_arr = [1,1]

    print(my_sol.findDisappearedNumbers(my_num_arr))
