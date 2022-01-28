def solution(l):
    """
    start with a number in the list
    compare to numbers > than it to find i mod n = 0
    then use i to repeat the process.
    save those, count those and they are the lucky triples
    """
    viable = 0
    # sol = []
    # tracking i's location is how we avoid
    # issues caused by repeating values
    i_loc = 0
    # solve corner cases
    if len(set(l)) == 1:
        return 1
    for i in l:
        k_loc = i_loc + 1
        for k in l[k_loc:]:
            if k % i == 0:
                for n in l[k_loc+1:]:
                    if n % k == 0:
                        #sol.append([i,k,n])
                        viable += 1
            k_loc += 1
        i_loc += 1
    return viable #, sol

solution([1,2,3,4,5,6])
# 3
solution([1,1,1])
# 1
import random
l = random.sample(range(1, 2001), 2000)
solution(l)
