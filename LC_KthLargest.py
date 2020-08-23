from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]) -> None:
        self._k = k
        self._nums = nums

    def __get_kth_largest(self) -> int:
        self._nums.sort(reverse=True)
        return self._nums[self._k-1]

    def add(self, n: int) -> int:
        self._nums.append(n)
        self.get_sorted_nums()
        return self.__get_kth_largest()

    def get_sorted_nums(self) -> None:
        print(sorted(self._nums, reverse=True))


if __name__ == '__main__':
    k = 3
    arr = [4, 5, 8, 2]

    obj = KthLargest(k, arr)
    obj.get_sorted_nums()
    print(obj.add(3))
    print(obj.add(5))
    print(obj.add(10))
    print(obj.add(9))
    print(obj.add(4))
