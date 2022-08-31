def solve(mat:list[list[int]])->list[list[int]]:
    directions=[[0,1],[1,0],[0,-1],[-1,0]]
    def dfs(x:int,y:int,visited:set(),old_el:int):
        key=(x,y)
        if 0<=x<row and 0<=y<col and key not in visited and mat[x][y]>=old_el:
            visited.add(key)
            for i,j in directions:
                dfs(x+i,y+j,visited,mat[x][y])
    
    row,col=len(mat),len(mat[0])
    p_visited=set()
    a_visited=set()
    for i in range(row):
        dfs(i,0,p_visited,mat[i][0])
        dfs(i,col-1,a_visited,mat[i][col-1])
    for i in range(col):
        dfs(0,i,p_visited,mat[0][i])
        dfs(row-1,i,a_visited,mat[col-1][i])    
    result=[]
    for i in range(row):
        for j in range(col):
            key=(i,j)
            if key in p_visited and key in a_visited:result.append(key)
    return result

mat=[
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]
print(solve(mat))