import math

def solution(n):
    """
    finding the nearest number that only has 2 as its prime factor
    seems likely to produce the optimal result

    this niave approach won't work since dividing by 2
    will also cut that remainder distance from 2^n in half, so
    it will always be better to get the number as small as possible
    via division until our "remainder" i.e. distance from 2^n == 1
    """
    # solve the easy ones
    n = int(n)
    if n == 0:
        return 0
    elif math.log(n, 2).is_integer():
        return int(math.log(n, 2))
    else:
        nearest = round(math.log(n, 2))
        dist = abs(n - 2**nearest)
        return int(dist + nearest)


solution('15')