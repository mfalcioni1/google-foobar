import itertools as iter

def solution(num_buns, num_required):
    """
    total keys = num_buns choose num_required-1

    no num_required-1 # of bunnies can have the ability
    to unlock the doors.
    this can lead us to how many times each key is held.
    looking at the examples, (5, 3) each key is held 3 times
    (3, 1) each key is held 3 times
    (2, 2) each key is held once
    (3, 2) each key is held twice
    (4, 4) each key is held once
    is it num_buns - num_required + 1?

    so each key in range(total_keys) needs to be held
    num_buns - num_required + 1 times.
    So we need to assign each key to num_required bunnies.

    this means each bunny holds (total_keys*dupe_keys)/num_buns keys
    
    for each of range(total_keys)
    choose dupe_keys num_bunnies to possess that key.
    are there always total_keys ways to select groups of dupe_keys bunnies?
    n = num_buns
    k = num_require
    j = n - k + 1 = dupe_keys
    n!/(k-1)!(n-(k-1))! = total_keys = C(n, k - 1)
    C(n, n-(k-1) = C(n, n - k + 1) = C(n, k - 1)

    yes, since we know C(n, k) = C(n, n-k)
    so it follows C(n, k - 1) = C(n, n - (k - 1)) = C(n, n - k + 1) = C(n, j)
    """

    dupe_keys = num_buns - num_required + 1
    sol = [[] for _ in range(num_buns)]
    
    # solve easy cases
    if num_buns == num_required:
        for i in range(num_required):
            sol[i] = [i]
        return sol
    if num_required == 1:
        for i in range(num_buns):
            sol[i] = [0]
        return sol
    if num_required == 0:
        return sol

    i = 0
    for l in iter.combinations(range(num_buns), dupe_keys):
        for j in l:
            sol[j].append(i)
        i += 1
    return sol

solution(5, 0)
solution(4, 1)
solution(4, 4)
solution(5, 3)