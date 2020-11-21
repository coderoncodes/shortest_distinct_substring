size = 123
def distictCh(str, n):
    count = [0]*size
    for i in range(n):
        count[ord(str[i])] += 1
    distinct = 0
    for i in range(size):
        if (count[i] != 0):
            distinct += 1
    return distinct

def sub(str):
    sizemax = len(str)
    maxDist = distictCh(str,sizemax)
    minlen = sizemax
    for i in range(sizemax):
        for j in range(sizemax):
            subs = str[i:j]
            lensub = len(subs)
            subDistinctCh =distictCh(subs,lensub)
            if (lensub < minlen and maxDist == subDistinctCh):
                minlen =lensub
    return minlen

print(sub(input()))