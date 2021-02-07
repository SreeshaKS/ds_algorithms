class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True

# Let's use the order of nodes in the inorder traversal Left -> Node -> Right.

# postorder

# Here the nodes are enumerated in the order you visit them, and you could follow 1-2-3-4-5 to compare different strategies.

# Left -> Node -> Right order of inorder traversal means for BST that each element should be smaller than the next one.

# Hence the algorithm with \mathcal{O}(N)O(N) time complexity and \mathcal{O}(N)O(N) space complexity could be simple:

# Compute inorder traversal list inorder.

# Check if each element in inorder is smaller than the next one.

# postorder

# Do we need to keep the whole inorder traversal list?

# Actually, no. The last added inorder element is enough to ensure at each step that the tree is BST (or not). Hence one could merge both steps into one and reduce the used space.