import challenge_header as CH


def rotate(nums: [int], k: int) -> [int]:
    nums_len = len(nums)
    if k % nums_len == 0:
        return nums
    '''
    for i in range(k):
        temp = nums[nums_len - 1]
        for 
    '''
    return [1]


if __name__ == "__main__":
    CH.printHeader("ROTATE Array")
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(rotate(nums, k))
