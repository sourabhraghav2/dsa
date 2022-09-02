from dsa.model import TreeNode
def solve(root: TreeNode) -> int:
    result=[]
    def find(root:TreeNode, value:int):
        if root:
            if root.val>=value:result.append(root.val)
            find(root.left,max(value,root.val))
            find(root.right,max(value,root.val))
    find(root,float('-inf'))
    return len(result)


root=TreeNode(3,TreeNode(1,TreeNode(3)),TreeNode(4,TreeNode(1),TreeNode(5)))
print(solve(root))