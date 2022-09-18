def solve(mat:list[list[int]],weak:int=0,max_d:int=0)->int:
    mat=sorted(mat,key=lambda x: (-x[0],x[1]))
    for a,d in mat:
        if(max_d>d):weak+=1
        max_d=max(max_d,d)
    return weak

print(solve([[3,10],[1,5],[7,7],[1,2],[7,3],[9,8],[8,10],[9,7],[4,3],[1,5]]))
# print(solve([[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]))

#Solution
#1. Sort attack from increasing to decreasing
#2. Traverse and keep finding heighest defense
#3. Same attack should not class with each other so for same attack level sort defence to increasing from decreasing  