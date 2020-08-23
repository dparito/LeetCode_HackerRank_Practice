import challenge_header as CH


def singleNumber(num_list) -> int:
    nums_set = set(num_list)
    for i in nums_set:
        if num_list.count(i) == 1:
            return i
        else:
            continue


if __name__ == "__main__":
    CH.printHeader("Single Number")

    num_list = [4, 1, 2, 1, 2]
    lone_num = singleNumber(num_list)
    print(lone_num if lone_num != -1 else "All numbers repeat")
