from challenge_header import printHeader


def findTwoSum(nums, target) -> None:
    two_indices = []
    for i in range(0, len(nums)):
        diff = target - nums[i]
        nums_left = nums[i+1:]
        if diff in nums_left:
            two_indices.append(i)
            two_indices.append(nums_left.index(diff) + i + 1)
            break
        else:
            continue
    print(two_indices)



if __name__ == "__main__":
    printHeader("Two Sum")

    nums = [3, 6, 3]
    target = 6
    findTwoSum(nums, target)
