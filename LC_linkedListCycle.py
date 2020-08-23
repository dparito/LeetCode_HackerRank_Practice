# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        pass


if __name__ == "__main__":
    mysol = Solution()
    
    linked_list_val = [3, 2, 0, -4]
    linked_list_nodes = []
    i = 1
    head = node = ListNode(linked_list_val[0])
    while i < len(linked_list_val):
        node.val = linked_list_val[i]
        node.next = ListNode(i+1)
        # print(node.val)
        i += 1
    
    while head:
        print(f"node = {head.val}")
        head = head.next
    
    

