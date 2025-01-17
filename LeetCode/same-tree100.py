# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import TreeNode
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is not None and q is not None:
            if p.val == q.val:
                return self.isSameTree(p.left,q.left) and \
                       self.isSameTree(p.right,q.right)
            else:
                return False
        else:
            return False
