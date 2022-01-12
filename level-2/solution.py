import heapq

def solution(xs):
    '''
    remove 0s and 1s
    find all positive integers
    if at least 2 negative numbers
        find the greatest even number of negative numbers
    product product as string
    '''
    negatives = [num for num in xs if num < 0]
    max_power = [num for num in xs if num > 0]

    if len(negatives) > 1 & (len(negatives) % 2) == 0:
        max_power = max_power + negatives

    elif len(negatives) > 1 & (len(negatives) % 2) == 1:
        negatives.remove(max(negatives))
        max_power = max_power + negatives

    # we always need to calculate max_power given one panel is off based on prompt.
    # i.e. "subset" -> A =/= B
    # this gets complicated with the posibility of the
    # product of the greatest two negatives numbers < smallest positive number
    if len(max_power) == len(xs):
        if len(negatives) > 0:
            positives = [num for num in xs if num > 0]
            if min(positives) > reduce(lambda y, z: y * z, heapq.nlargest(2, negatives)):
                negatives.remove(heapq.nlargest(2, negatives))
            else:
                positives.remove(min(positives))
                max_power = positives + negatives
        else:
            max_power.remove(min(max_power))

    # 0 can be a max power.
    if len(max_power) == 0:
       output = str(0)

    else: 
        output = str(reduce(lambda y, z: y * z, max_power))

    return output


# Tests
# solution([2, 0, 2, 2, 0])
# 8
# solution([-2, -3, 4, -5])
# 60
# solution(range(-1000, 1000))
# some large number
# solution([0, 0, 0, -1])
# 0
# solution([0, 0, -1, -1])
# 1
# solution([1, 0, 1, -1])
# 1
# solution([-3, -4, 3, 4, 5])
# 240
# solution([-3, -4, 3, 4, 5, 1])
# 720
# solution([2, 1, 2, 2, 1])
# 8
# solution([-2, -3, -4, -5, 1, 2, 3, 4])
# 2880
# solution([-2, -3, -4, -5, 2, 3, 4])
# 1440
# solution([-2, -3, 7, 8, 9])
# wrong: 336; 