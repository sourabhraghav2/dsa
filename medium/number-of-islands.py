def solve(mat:list[list[str]])->int:
    row,col=len(mat),len(mat[0])
    in_boundaries=lambda x,y: 0<=x<row  and 0<=y<col  and mat[x][y]!='X' 
    def visit(x: int,y:int):
        if in_boundaries(x,y) and mat[x][y]=='1':
            mat[x][y]='X'
            visit(x+1,y)
            visit(x,y+1)
            visit(x-1,y)
            visit(x,y-1)
    count=0
    for x in range(row):
        for y in range(col):
            if mat[x][y]=='1':count+=1
            visit(x,y)
            print(mat)
    return count


# mat=[
#         ["1","1","1","1","0"],
#         ["1","1","0","1","0"],
#         ["1","1","0","0","0"],
#         ["0","0","0","0","0"]
#     ]
# mat=[
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# mat=[
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# mat=[["0"]]
mat=[
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
    ]
print(solve(mat))