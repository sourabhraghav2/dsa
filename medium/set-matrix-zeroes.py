def solve(mat:list[list[int]])->None:
    row,col=len(mat),len(mat[0])
    firstCol=False
    for i in range(row):
        if mat[i][0]==0:firstCol=True
        for j in range(1,col):
            if mat[i][j]==0:
                mat[0][j]=0
                mat[i][0]=0
    for i in range(1,row):
        for j in range(1,col):
            if mat[0][j]==0 or mat[i][0]==0:mat[i][j]=0
    if mat[0][0]==0:
        for j in range(1,col):
            mat[0][j]=0
    if firstCol:
        for i in range(row):
            mat[i][0]=0

mat=[[1,1,1],[1,0,1],[1,1,1]]
mat=[[3,1,0,5,9],[3,4,5,2,8],[1,3,1,5,2]]
mat=[[1,1,1],[1,0,1],[1,1,1]]
solve(mat)