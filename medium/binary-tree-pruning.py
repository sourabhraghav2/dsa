from dsa.model import TreeNode
def solve(root:TreeNode) ->TreeNode:
    def find(node:TreeNode)->bool:
        if not node:return 0
        left=find(node.left)
        right=find(node.right)
        if left==0:node.left=None
        if right==0:node.right=None
        return 0 if node.val==0 and left==0 and right==0 else 1
    return root if find(root)!=0 else None

root=TreeNode(1,None,TreeNode(0,TreeNode(0),TreeNode(1)))
print(solve(root))