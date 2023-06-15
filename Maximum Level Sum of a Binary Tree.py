Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
# Use Level Order Traversal
def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        que = deque()
        que.append(root)
        ans = float('-inf')
        level = 0
        count = 0

        while len(que) > 0:
            count += 1
            temp = 0
            n = len(que)
            while n:
                node = que.popleft()
                temp += node.val
                if node.left != None:
                    que.append(node.left)
                if node.right != None:
                    que.append(node.right)
                n -= 1

            if ans < temp:
                level = count
                ans = temp
        return level
        
