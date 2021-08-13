memoization = {}
def go(i,j,s):
    
    if (i>j):
         return  1
    if (i==j):
        return 1
    if (s[i]!=s[j]):
        return 0
    if (str(i) + " " + str(j)) in memoization:
        return memoization[str(i) + " " + str(j)]
    ans = go(i+1,j-1,s)
    memoization[str(i) + " " + str(j)] = ans
    print(memoization)
    return  ans

s =input()
str_len = len(s)
ans = 0
for i in range(str_len):
    for j in range(i,str_len):
        ans+=go(i,j,s)
print(ans)