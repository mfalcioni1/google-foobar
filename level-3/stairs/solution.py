import itertools

def solution(n):
    '''
    x = # steps; s_x = bricks in stair x; 
    n = # ttl bricks; s_X = array of all stairs' bricks;
    max_h1 = maximum height of stair 1;
    min_h1 = minumum height of stair 1;
    max_x = maximum number of steps
    min_x = minimum number of steps
    r_n = remaining stairs

    Constraints:
    x >= 2
    s_x =/= s_i
    s_1 > ... > s_i
    max_h <= n-1
    min_h = 2
    max_x s.t. sum(seq(1,x)) <= n
    min_x = 2
    min_h1 s.t. n >= sum(seq(1, x))
    max_h1 = n-1
    sum(s_X) = n
    '''
    # set-up some of the constraints
    min_h = 2
    min_x = 2
    max_h1 = n-1
    # first find max_x and min_h1 for n
    mini = True
    k = 2
    while mini:
        if n > sum(range(1, k)):
            k += 1
        else:
            max_x = k-1
            min_h1 = k-1
            mini = False

    '''
    def create_stair(min_hx, max_hx):
        s_x = range(min_hx, max_hx+1)
        return s_x
    itertools.combinations(range(min_h1, max_h1+1), 2)

    Stuckish, probably need some type of recursive
    function to create all the possible stair sets.
    '''
    # start creating solutions
    viable = 0
    val = []
    for x in range(2, max_x+1):
        s_X = [None for _ in range(x)]
        for x_i in range(1, x+1):
            if x_i == 1:
                val = range(min_h1, max_h1+1)
                n_r = [n - c for c in val]
            
        for s_1 in range(min_h1, max_h1+1):
            s_X[0] = s_1
            r_n = n - s_1

            if sum(c is None for c in s_X) == 1:



# Input:
solution(200)
# Output:
#    487067745

# Input:
solution(3)
# Output:
#    1