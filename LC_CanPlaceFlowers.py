from typing import List


class Solution:

    @classmethod
    def canPlaceFlowers(cls, flowerbed: List[int], n: int) -> bool:
        fb_len = len(flowerbed)
        possible = False

        if n == 0:
            return True

        if n > fb_len:
            return False

        if 3 > fb_len == n and flowerbed.count(1) > 0:
            return False

        for fl in range(n):
            empty_spot_ends = [0, 0]
            if flowerbed[:2] == empty_spot_ends:
                flowerbed[0] = 1
                possible = True
                continue

            if flowerbed[-2:] == empty_spot_ends:
                flowerbed[-1] = 1
                possible = True
                continue

            empty_spot_middle = [0, 0, 0]
            for i in range(1, fb_len - 1):
                if empty_spot_middle == flowerbed[i - 1:i + 2]:
                    flowerbed[i] = 1
                    possible = True
                    break
                else:
                    possible = False
        return possible

    @classmethod
    def getEmptySlotCount(cls, flowerbed: List[int]) -> int:
        slot = [0] * len(flowerbed)
        return sum(1 for i in range(len(flowerbed)) if flowerbed[i:i + len(slot)] == slot)


if __name__ == '__main__':
    sol = Solution()

    flowerbed = [1, 0, 0, 0, 0, 0, 0, 0, 1]
    n_flowers = 4
    flowerbed = [0, 0, 1, 0, 1]
    flowerbed = [0, 0]
    n_flowers = 2

    # print(sol.getEmptySlotCount(flowerbed))

    print(sol.canPlaceFlowers(flowerbed, n_flowers))
