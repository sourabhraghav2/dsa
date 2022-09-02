from dsa.model import TreeNode
from collections import defaultdict
def solve(root: TreeNode)->list[float]:
    answer=defaultdict(lambda:[])
    def find(node: TreeNode,level:int=0):
        nonlocal answer
        if node:
            answer[level].append(node.val)
            find(node.left,level+1)
            find(node.right,level+1)
    find(root)
    return [sum(each)/len(each) for each in answer.values()]


root=TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
print(solve(root))