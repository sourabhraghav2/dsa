def solve(mat:list[int])->list[int]:
    for i in range(len(mat)):
        for j in range(i):mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
    for index in range(len(mat)):
        i,n=0,len(mat[0])-1
        while i<n:
            mat[index][i],mat[index][n]=mat[index][n],mat[index][i]
            i+=1
            n-=1
    return mat
    
input=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
print(solve(input))
