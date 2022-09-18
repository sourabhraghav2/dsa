def solve( n: int,mat=[]) -> list[list[int]]:
    for i in range(n):
        inner=[1]
        for j in range(1,i):inner.append(mat[i-1][j-1]+mat[i-1][j])
        if i!=0:inner.append(1)
        mat.append(inner)
    return mat

print(solve(7))


# [
#                     [(0, 0)], 
#                 [(1, 0), (1, 1)], 
#             [(2, 0), (2, 1), (2, 2)], 
#         [(3, 0), (3, 1), (3, 2), (3, 3)], 
#     [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)], 
# [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]
# ]
#VoidTransaction(