def solve(arr:list[int])->list[int]:
    length=len(arr)
    def find(start,end):
        mid=start
        while mid<=end:
            match arr[mid]:
                case 0:
                    arr[start],arr[mid]=arr[mid],arr[start]
                    find(start+1,end)
                    break
                case 1:mid+=1
                case 2:
                    arr[end],arr[mid]=arr[mid],arr[end]
                    find(start,end-1)
                    break
    find(0,length-1)
    return arr

# print(solve([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))
print(solve([2,0,2,1,1,0]))