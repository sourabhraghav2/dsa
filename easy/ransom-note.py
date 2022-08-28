from collections import defaultdict


def solve(note:str, mag:str)->bool:
    WC=defaultdict(lambda: 0)
    for e in note:WC[e]+=1
    for e in mag:WC[e]-=1
    for v in WC.values():
        if v>0:return False 
    return True
        
print(solve("a","b"))
print(solve("aa","ab"))
print(solve("aa","aab"))
print(solve("aab","baa"))
print(solve("aa","aab"))