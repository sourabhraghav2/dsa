def solve(arr:list[int])->list[int]:
    def reverse(l:int,r:int):
        while l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
    def swap(l,r):arr[l],arr[r]=arr[r],arr[l]
    r=len(arr)-2
    while r>=0:
        if arr[r]<arr[r+1]:break
        r-=1
    if r==-1:reverse(0,len(arr)-1)
    else:
        l,r=r,len(arr)-1
        while l<r and arr[l]>=arr[r]:
            r-=1
        swap(l,r)
        reverse(l+1,len(arr)-1)
    return arr
    
# print(solve([1,2,3]))
# print(solve([3,2,1]))
# print(solve([1,2,3,5,4,2]))
print(solve([1,5,1]))