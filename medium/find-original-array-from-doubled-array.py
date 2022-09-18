from collections import defaultdict
def solve(arr:list[int],store=defaultdict(lambda:0))->list[int]:
    answer=[]
    arr.sort
    for each in arr:
        if store[(each/2)]>0:
            store[(each//2)]-=1
            answer.append(each//2)
        elif store[each*2]>0:
            store[each*2]-=1
            answer.append(each)
        else:store[each]+=1
    print(store)
    return [] if max(store.values())>0 else answer

# print(solve([1,3,4,2,6,8]))
# print(solve([0,0,0,0]))
# print(solve([2,1]))
# print(solve([2,2,1,1]))
print(solve([4,4,16,20,8,8,2,10]))
