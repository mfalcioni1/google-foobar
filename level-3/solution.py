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

    # if root, return -1 
    if q == e:
        p = -1
    # go into search
    else:
        loc = e
        i = 1
        while i < h:
            if q == loc-2**(h-i) | q == loc-1:
                p = loc
                i = h
            elif q > loc-2**(h-i):
                loc = loc-1
                i += 1
            else:
                loc = loc-2**(h-i)
                i += 1
    return p

solution(3, 3)

'''
   7
 3   6
1 2 4 5

                         31
          15                            30
     7          14              22              29
  3     6    10     13      18      21      25      28
1  2  4  5  8  9  11  12  16  17  19  20  23  24  26  27
'''