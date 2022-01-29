def slow_solution(l):
    viable = 0
    # tracking i's location is how we avoid
    # issues caused by repeating values
    i_loc = 0
    # solve corner cases
    if len(l) == 2:
        return 0
    #if len(set(l)) == 1:
    #    return 1
    for i in l:
        k_loc = i_loc + 1
        for k in l[k_loc:]:
            if k % i == 0:
                for n in l[k_loc+1:]:
                    if n % k == 0:
                        viable += 1
            k_loc += 1
        i_loc += 1
    return viable

slow_solution(range(1, 7))