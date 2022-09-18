def solve(arr:list[list[int]])->list[list[int]]:
    arr=sorted(arr,key=lambda x:x[0])
    answer=[]
    print(arr)
    for i in range(len(arr)-1):
        current,next=arr[i],arr[i+1]
        print(current," : ",next)
        if current[1]<next[0]:answer.append(current)
        else:arr[i+1]=[min(current[0],next[0]),max(current[1],next[1])]
    answer.append(arr[-1])
    return answer

# print(solve([[1,3],[2,6],[8,10],[15,18]]))
print(solve([[1,4],[0,0]]))
#[[1,6],[8,10],[15,18]]