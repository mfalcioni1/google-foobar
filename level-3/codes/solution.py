def solution(l):
    """
    start with a number in the list
    compare to numbers > index than it to find i mod n = 0
    then use i to repeat the process.
    save those, count those and they are the lucky triples
    first solution might be too slow with 3 loops? O(n^3)
    new idea, looking backwards how many divisors does
    the previous number have given the current number is
    divisible by it. This will cut out a iteration in the loop
    since we will be keeping track of previously discovered
    divisors.
    """
    viable = 0
    # tracking i's location is how we avoid
    # issues caused by repeating values
    i_loc = 0
    # set up array to track how many previous
    # divisors the ith number has.
    divisors = [0 for _ in range(len(l))]
    # solve corner cases
    if len(l) == 2:
        return 0
    for i in l:
        k_loc = 0
        for k in l[0:i_loc]:
            if i % k == 0:
                divisors[i_loc] += 1
                # the number of viable solutions is
                # equal to the number of viable divisors
                # k has once it passes this condition
                # plus previous viable solutions.
                viable += divisors[k_loc]
            k_loc += 1
        i_loc += 1
    return viable

solution([1,2,3,4,5,6])
# 3
solution([1,1,1])
# 1
solution([1,1,1,1])
l = range(1, 7)
solution(l)
import random
l = random.sample(range(1, 2001), 2000)
solution(l)
l = []
r = range(1, 26)
r = 1
while len(l) <= 2000:
    l.append(random.choice(r))
solution(l)