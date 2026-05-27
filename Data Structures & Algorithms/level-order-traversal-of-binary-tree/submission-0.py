# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)
        while q:
            q_len = len(q)
            tmp = []
            for i in range(q_len):
                n = q.popleft()

                if n:
                    tmp.append(n.val)
                    q.append(n.left)
                    q.append(n.right)

            if tmp:
                res.append(tmp)

        return res
        