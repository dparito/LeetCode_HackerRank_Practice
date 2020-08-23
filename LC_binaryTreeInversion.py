from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def arrayToTree(self, arr: List[int]) -> TreeNode:
        for i in arr:
            

    def invertTree(self, root: TreeNode) -> TreeNode:
        return root


if __name__ == '__main__':
    my_sol = Solution()

    bi_tree_arr = [4, 2, 7, 1, 3, 6, 9]

    bi_tree_root = arrayToTree(bi_tree_arr)

    inverted_bi_tree = my_sol.invertTree(bi_tree_root)
