import itertools

def solution(dimensions, your_position, trainer_position, distance):
    """
    Figure out the max number of bounces a shot can take given distance
    constraint?
    There has to be some property vectors originating from each point and
    the angle they produce when intersecting on of the walls

    https://www.sciencedirect.com/topics/mathematics/angle-between-two-vector
    https://en.wikipedia.org/wiki/Angle_of_incidence_(optics)
    movement is alot like billiards table
    https://en.wikipedia.org/wiki/Dynamical_billiards

    https://mathworld.wolfram.com/Billiards.html

    http://pi.math.cornell.edu/~mec/Summer2009/Remus/lesson1.html

    https://www.khanacademy.org/math/geometry/hs-geo-similarity/hs-geo-similar-and-congruent-triangles-modeling/v/triangle-similarity-in-pool
    https://en.wikipedia.org/wiki/Carom_billiards
    
    https://undergroundmathematics.org/thinking-about-geometry/r8022/solution
    Method 1 from this link creates a helpful visual. 
    https://blogs.scientificamerican.com/roots-of-unity/how-to-unfold-a-pool-table/
    https://plus.maths.org/content/arithmetic-billiards-0
    Combined with this I think there is a concept that can be applied, "unfolding the billiards table"
    with each "fold" (reflection of the table off a given wall) we replace our opponent in space
    then after "x" folds we calculate the distance between us and the folded opponent
    if it is < distance constraint then it is a viable solution.

    This works. I do have to figure out a way to check that you don't hit yourself.
    Slope is the answer to how you check if you risk bouncing into yourself.

    Working through understanding possible solutions.
    Each additional carom adds 4 + (n) solutions, where n is the previous
    number of caroms number of solutions, i.e. 1 carom=4, 2 carom=8
    if we can create all the possible direction profiles for a given
    number of caroms we can call our couple functions as we loop through
    them to get the answer. Main issue is that n -> e is the same as e -> n.
    So they are combinations, but also you can't select the opposite of the
    previous option. i.e. n -> s is not viable.
    """

    def e_dist(p_1, p_2):
        return ((p_2[0] - p_1[0])**2 + (p_2[1] - p_1[1])**2)**0.5
    
    def l_dist(p_1, p_2):
        return abs(p_1 - p_2)
    
    def slope_check(your_position, n_yp, n_tp, dimensions):
        def slope(p_1, p_2):
            if (p_2[0] - p_1[0]) == 0:
                s = None
            else:
                s = float(p_2[1] - p_1[1])/float(p_2[0] - p_1[0])
            return s
        s_tp = slope(your_position, n_tp)
        s_yp = slope(your_position, n_yp)
        if n_tp[0] > 0 and n_tp[1] > 0:
            s_corner = slope(your_position, [dimensions[0], dimensions[1]])
        elif n_tp[0] < 0 and n_tp[1] > 0:
            s_corner = slope(your_position, [0, dimensions[1]])
        elif n_tp[0] <= 0 and n_tp[1] <= 0:
            s_corner = slope(your_position, [0, 0])
        elif n_tp[0] > 0 and n_tp[1] < 0:
            s_corner = slope(your_position, [dimensions[0], 0])
        if s_tp == s_yp or s_corner == s_tp:
            return 0
        else:
            return 1
    
    def s_fold(yp, tp, walls):
        n_yp = [yp[0], yp[1] - 2*l_dist(yp[1], walls['s'])]
        n_tp = [tp[0], tp[1] - 2*l_dist(tp[1], walls['s'])]
        n_walls = {'n': walls['s'], 's': walls['s'] - dimensions[1], 'e': walls['e'], 'w': walls['w']}
        return n_yp, n_tp, n_walls
    
    def n_fold(yp, tp, walls):
        n_yp = [yp[0], yp[1] + 2*l_dist(yp[1], walls['n'])]
        n_tp = [tp[0], tp[1] + 2*l_dist(tp[1], walls['n'])]
        n_walls = {'n': walls['n'] + dimensions[1], 's': walls['n'], 'e': walls['e'], 'w': walls['w']}
        return n_yp, n_tp, n_walls
    
    def e_fold(yp, tp, walls):
        n_tp = [tp[0] + 2*l_dist(tp[0], walls['e']), tp[1]]
        n_yp = [yp[0] + 2*l_dist(yp[0], walls['e']), yp[1]]
        n_walls = {'n': walls['n'], 's': walls['s'], 'e': walls['e'] + dimensions[0], 'w': walls['e']}
        return n_yp, n_tp, n_walls
    
    def w_fold(yp, tp, walls):
        n_tp = [tp[0] - 2*l_dist(tp[0], walls['w']), tp[1]]
        n_yp = [yp[0] - 2*l_dist(yp[0], walls['w']), yp[1]]
        n_walls = {'n': walls['n'], 's': walls['s'], 'e': walls['w'], 'w': walls['w'] - dimensions[0]}
        return n_yp, n_tp, n_walls

    folds = {
        'n': n_fold,
        's': s_fold,
        'e': e_fold,
        'w': w_fold
    }

    def folder(yp, tp, walls, path):
        for p in path:
            yp, tp, walls = folds[p](yp, tp, walls)
        return yp, tp, walls

    def eval(yp, fo, distance):
        if (slope_check(yp, fo[0], fo[1], dimensions) == 1) and (e_dist(yp, fo[1]) <= distance):
            return 1
        else:
            return 0

    sols = []
    if e_dist(your_position, trainer_position) <= distance:
        sols.append(trainer_position)
    else:
        return 0

    walls = {'n': dimensions[1], 's': 0, 'e': dimensions[0], 'w': 0}
    folding = True
    carom = 1
    n_sols = 0
    while folding:
        folding = False
        for p in itertools.combinations_with_replacement('nsew', carom):
            fold = folder(your_position, trainer_position, walls, path = p)
            if eval(your_position, fold, distance) == 1:
                sols.append(fold[1])
        sols = [list(x) for x in set(tuple(x) for x in sols)]
        if n_sols < len(sols):
            n_sols = len(sols)
            folding = True
            carom += 1

    return n_sols

# test case
# dimensions, your_position, trainer_position, distance = [3, 2], [1, 1], [2, 1], 4
# dimensions, your_position, trainer_position, distance = [300,275], [150,150], [185,100], 500
dimensions, your_position, trainer_position, distance = [2, 5], [1, 2], [1, 4], 6
solution([3, 2], [1, 1], [2, 1], 4)
solution([300,275], [150,150], [185,100], 500)

solution([2, 5], [1, 2], [1, 4], 11) # 27
solution([2, 5], [1, 2], [1, 4], 6) # 7
solution([23, 10], [6, 4], [3, 2], 23) # 8

#[[-3, 6]wwn, [5, 4]ee, [5, 6]een, [3, 6]en, [-1, 4]w, [-3, 4]ww, [3, 4]e, [-1, 6]wn]
p = ['w', 'w']
fold = folder(your_position, trainer_position, walls, path = p)
fold
eval(your_position, fold, distance)
slope_check(your_position, fold[0], fold[1], dimensions)
e_dist(your_position, fold[1]) <= distance