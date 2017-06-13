class Node:

    def __init__(self, data):

        self.right = self.left = None
        self.data = data


class Solution:

    def insert(self, root, data):

        if root == None:
            return Node(data)

        else:

            if data <= root.data:

                cur = self.insert(root.left, data)
                root.left = cur

            else:

                cur = self.insert(root.right, data)
                root.right = cur

        return root

    def levelOrder(self, root):
        # Write your code here
        queue = [root]

        while queue:

            current = queue.pop()
            print current.data,

            if current.left:
                queue.insert(0, current.left)

            if current.right:
                queue.insert(0, current.right)

T = int(raw_input())
myTree = Solution()
root = None
for i in range(T):
    data = int(raw_input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
