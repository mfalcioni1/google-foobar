
def solution(h, q):
    '''
    check if root
    then check left and right
        right is loc-1 left if loc-2^(h-i)
    else decide left or right
    repeat until through tree
    to do it for array check whole array?
    '''

    e = 2**h - 1 #number of nodes in tree

    # allocate solution array
    p = [None for _ in range(len(q))]

    # if root, return -1 
    if e in q:
        p[q.index(e)] = -1
    # go into search
    # TODO: solve for repeated value case.
    else:
        loc = e
        i = 1
        while i < h:
            if q in loc-2**(h-i):
                p[q.index(loc-2**(h-i))] = loc
            elif q in loc-1:
                p[q.index(loc-1)] = loc
            elif q > loc-2**(h-i):
                loc = loc-1
                i += 1
            else:
                loc = loc-2**(h-i)
                i += 1
    return p

    