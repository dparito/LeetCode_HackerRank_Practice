from challenge_header import printHeader


def containsDuplicate(nums) -> bool:
    nums_set = set(nums)
    return False if len(nums_set) == len(nums) else True


if __name__ == "__main__":
    printHeader("Contains Duplicate")
    nums = [1,2,3,1]
    print(containsDuplicate(nums))
