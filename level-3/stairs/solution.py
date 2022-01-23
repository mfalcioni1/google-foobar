def solution(n):
    '''
    https://en.wikipedia.org/wiki/Partition_(number_theory)
    https://oeis.org/A000009
    https://www.whitman.edu/mathematics/cgt_online/book/section03.03.html
    The partition of n into unique parts can be determined by the
    polynomial expansion of (1+x)...(1+x^n) and finding the
    coefficient of x^n, -1 since the math counts the base case.

    if we have a vector that represents the orders of the polynomials
    i.e. [0, 1] for 1+x
    we can calculate what introducing (1+x^2) would be
    [0, 1] + 2 = [2, 3] and then concat that to the original
    we would also maintain a vector of the coefficients
    [0, 1, 2, 3]; [1, 1, 1, 1]

    algo would be:
    order = [0]
    coef = []
    for i in 1:n+1:
        n_order = order + i
        order += n_order)
        for j in 0:n+1:
            coef[j] += order.count(j)-1
        order = list(set(order))
    return coef[n]-1
    ^^this draft was wrong due to not previous coef
    not being tracked during new expansion but it was
    good enough to get through it
    '''

    order = [0]
    coef = [0 for _ in range(0, n+1)]
    coef[0] = 1
    for i in range(1, n+1):
        n_order = [x + i for x in order]
        o_coef = list(coef)
        # no need to count exponents greater than n
        for j in filter(lambda k: k <= n, n_order):
            # new coef calc to sum prev coefs that come with
            # new orders
            coef[j] = coef[j] + o_coef[n_order.index(j)]
        order += n_order
        order = list(set(order))
    return coef[n]-1

# Input:
solution(200)
# Output:
#    487067745

# Input:
# solution(3)
# Output:
#    1
# solution(7)
# solution(8)
solution(9)
solution(10)