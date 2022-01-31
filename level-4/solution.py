def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    Obtained from https://stackoverflow.com/a/3025547
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

def solution(num_buns, num_required):
    """
    total keys = num_buns choose num_required
    each key must be possessed num_required times
    This means each rabbit must hold (total_key*num_required)/num_buns keys
    
    possibly create the sets iteratively?
    set 1 is always range(0,(total_key*num_required)/num_buns)

    """

    total_keys = choose(num_buns, num_required)
    keys_held = (total_keys*num_required)/num_buns
    sol = [[] for i in range(num_buns)]
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


solution(5, 0)
solution(4, 1)
solution(4, 4)