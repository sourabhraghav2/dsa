from dsa.model import TreeNode
from collections import defaultdict
from functools import reduce
from dsa.util import createTree,levelOrder

flat_map = lambda f, xs: reduce(lambda a, b: a + b, map(f, xs))
def solve(root: TreeNode)->list[list[int]]:
    v_traverse=defaultdict(lambda: defaultdict(list))
    def find(node:TreeNode, direction:int,depth:int):
        if node:
            v_traverse[direction][depth].append(node.val)
            find(node.left,direction-1,depth-1)
            find(node.right,direction+1,depth-1)
    find(root,0,0)
    result=[]
    for key in sorted(v_traverse.keys()):
        inner=[]
        for each in v_traverse[key].values():inner=inner+sorted(each)
        result.append(inner)
    return result

root=TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
root=TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(6)),TreeNode(3,TreeNode(5),TreeNode(7)))
print(solve(root))

#[0,8,1,None,None,3,2,None,4,5,None,None,7,6]
