from collections import defaultdict
def solve(mat: list[list[int]]) -> list[list[int]]:
    D=defaultdict(list)
    row,col=len(mat),len(mat[0])
    for i in range(row):
        for j in range(col):
            D[i-j].append(mat[i][j])
    for each in D:
        D[each].sort(reverse=True)
    for i in range(row):
        for j in range(col):
            mat[i][j]=D[i-j].pop()
    return mat

mat=[[3,3,1,1],[2,2,1,2],[1,1,1,2]]
print(solve(mat))