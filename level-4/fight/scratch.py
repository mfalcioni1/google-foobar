import itertools
from math import atan2

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

    One additional fix, tracking slope makes things slightly easier
    than tracking bearings, however slopes can be duplicated.
    We will track angle trajectories instead.
    
    Pretty sure the solution is correct, and is just computationally
    inefficient.
    """

    def e_dist(p_1, p_2):
        return ((p_2[0] - p_1[0])**2 + (p_2[1] - p_1[1])**2)**0.5
    
    def l_dist(p_1, p_2):
        return abs(p_1 - p_2)
    
    def slope(p_1, p_2):
        if (p_2[0] - p_1[0]) == 0:
            s = None
        else:
            s = float(p_2[1] - p_1[1])/float(p_2[0] - p_1[0])
        return s

    def slope_check(your_position, n_yp, n_tp, dimensions):
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

    def fold_options(carom):
        paths = []
        # paths[0]=n, paths[1]=e, paths[2]=s, paths[3]=w
        for i in range(0, carom+1):
            paths.append([i, carom-i, 0, 0])
            paths.append([i, carom-i, 0, 0][::-1])
        if i > 0 and i < 3:
            paths.append([0, carom-i, i, 0])
            paths.append([i, 0, 0, carom-i])
        return paths

    folds = {
        0: n_fold,
        1: e_fold,
        2: s_fold,
        3: w_fold
    }

    def folder(yp, tp, walls, path):
        for f in range(len(path)):
            for n in range(path[f]):
                yp, tp, walls = folds[f](yp, tp, walls)
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
        for p in fold_options(carom):
            fold = folder(your_position, trainer_position, walls, path = p)
            if eval(your_position, fold, distance) == 1:
                if fold[1] not in sols:
                    sols.append(fold[1])
        if n_sols < len(sols):
            n_sols = len(sols)
            folding = True
            carom += 1

    return n_sols