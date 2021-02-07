# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValid(self, root, arr ,i , n):
        if i > n-1:
            return False
        
        if root.right is None and root.left is None and i == n-1:
            return root.val == arr[i]
        else:
            if root.val == arr[i]:
                if root.right is not None:
                    if self.isValid(root.right, arr, i+1,n):
                        return True
                if root.left is not None:
                    if self.isValid(root.left, arr, i+1,n):
                        return True
        return False

    def isValidSequence(self, root, arr):
        return self.isValid(root, arr, 0, len(arr))