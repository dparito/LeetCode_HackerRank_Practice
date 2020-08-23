# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# RECURSIVE MERGE SORT
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == "__main__":
    my_solution = Solution()
    l1 = ListNode(1)
    l12 = ListNode(2)
    l13 = ListNode(4)
    l1.next = l12
    l12.next = l13

    l2 = ListNode(1)
    l22 = ListNode(3)
    l23 = ListNode(4)
    l2.next = l22
    l22.next = l23

    # my_solution.mergeTwoLists(l1, l3)

    merged_list = my_solution.mergeTwoLists(l1, l2)

    while True:
        print(f'{merged_list.val}', end=' ')
        if merged_list.next == None:
            break
        merged_list = merged_list.next
