class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        combined_list = []
        for n in nums1:
            combined_list.append(float(n))
        
        for n in nums2:
            combined_list.append(float(n))
        
        combined_list.sort()
        total_ele = len(combined_list)
        mid_index = int(total_ele/2)
        if total_ele % 2 == 0:
            median = float((combined_list[mid_index] + combined_list[mid_index - 1]) / 2)
        else:
            median = combined_list[mid_index]
        return median


if __name__ == "__main__":
    nums1 = list(input().split())
    nums2 = list(input().split())
    test1 = Solution()
    print (test1.findMedianSortedArrays(nums1, nums2))