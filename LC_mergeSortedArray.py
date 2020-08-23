import challenge_header as CH


def merge(nums1, m: int, nums2, n: int) -> None:
    # TODO: merge the 2 sorted array; Assume: len(nums1) = m+n
    j = 0
    for i in range(m, m+n, 1):
        nums1[i] = nums2[j]
        j += 1
    nums1.sort()
    print(*nums1)


def main():
    CH.printHeader("Merge Sorted Array")
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    merge(nums1, 3, nums2, len(nums2))


if __name__ == "__main__":
    main()
