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
    # solve the easy one
    n = int(n)
    if n == 0:
        return 0
    else:
        i = 0 # tracking actions taken
        while n != 1:
            nearest = round(math.log(n, 2))
            dist = n - 2**nearest
            # if it is even divide by 2.
            if abs(dist) == 1:
                if n == 3: # 3 breaks the rule since it is closer to 2^2
                    n = n - 1
                    i += 1
                else:
                    n = n - dist
                    i += 1
            # if remainder is 0 then found solution
            elif dist == 0:
                return i + int(round(math.log(n, 2)))
            # if even divide by 2
            else:
                if n % 2 == 0:
                    n = n // 2
                    i += 1
                # need to decide whether to subtract or add 1
                # after doing some by hand it seems there is a trend
                # when adding, 13, 21, 25 end up wrong because subtraction
                # is the shortest path. it seem mod 4 = 1 should be subtraction 
                elif n % 4 != 1:
                    n = n + 1
                    i += 1
                else:
                    n = n - 1
                    i += 1
        return i

solution('15')
# 5
solution('17')
# 5
solution('18')
# 5
solution('20')
# 5
solution('4')
# 2
solution('131')
# 9
solution('13')
# 5