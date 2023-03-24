# space O(n+m)
# time o(2^(n+m))| n = len of array one and m = len of array two

def interweavingStrings(one,two,three):
    if len(three) != len(one) + len(two):
        return False
    return areInterwoven(one,two,three,0,0)
def areInterwoven(one,two,three,i,j):
    k = i + j 
    if k ==len(three):
        return True
    
    if i < len(one) and one[i]==three[k]:
        if areInterwoven(one,two,three, i+1, j):
            # does not need k+1 cuz i+ will also increase j
            return True
    
    if j < len(two) and two[j]==three[k]:
        return areInterwoven(one,two,three, i, j+1)
    
    return False