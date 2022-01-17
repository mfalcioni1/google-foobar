def solution(h, q):
    '''
    check if root
    then check left and right
        right is loc-1 left if loc-2^(h-i)
    else decide left or right
    repeat until through tree
    loop for each element of q (slow)
    '''

    e = 2**h - 1 #number of nodes in tree

    # allocate solution array
    p = [None for _ in range(len(q))]

    # if root, return -1 
    for x in q:
        if x == e:
            p[q.index(x)] = -1
        # go into search
        else:
            loc = e
            i = 1
            while i < h:
                if x == loc-2**(h-i) or x == loc-1:
                    p[q.index(x)] = loc
                    i = h
                elif x > loc-2**(h-i):
                    loc = loc-1
                    i += 1
                else:
                    loc = loc-2**(h-i)
                    i += 1
    return p

solution(3, [7, 3, 5, 1])
solution(5, [30, 5, 2])

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