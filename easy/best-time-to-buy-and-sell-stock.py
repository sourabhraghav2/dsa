def solve(arr:list[int])->int:
    current_min,max_benifit=float('inf'),0
    for each in arr:
        current_min=min(each,current_min)
        max_benifit=max(max_benifit,each-current_min)
    return max_benifit

# print(solve([7,1,5,3,6,4]))
print(solve([7,6,4,3,1]))