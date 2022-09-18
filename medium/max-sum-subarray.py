def solve(arr:list[int])->int:
    current_max=float('-1')
    current_max=float('-1')
    for each in arr:
        current_max=each if each+current_max<0 else current_max+each
        current_max
    return MAX

print(solve([-2,1,-3,4,-1,2,1,-5,4]))
