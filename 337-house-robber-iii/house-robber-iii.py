class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return 0, 0 # rob, not_rob
            l_rob, l_not = dfs(node.left)
            r_rob, r_not = dfs(node.right)
            rob = node.val + l_not + r_not
            not_rob = max(l_rob, l_not) + max(r_rob, r_not)
            return rob, not_rob

        return max(dfs(root))