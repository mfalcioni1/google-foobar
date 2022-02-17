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
    """
    def e_dist(p_1, p_2):
        return ((p_2[0] - p_1[0])**2 + (p_2[1] - p_1[1])**2)**0.5
    
    def l_dist(p_1, p_2):
        return p_1 - p_2
    
    def slope_check(your_position, n_tp, n_yp):
        s_tp = (your_position[1] - n_tp[1])/(your_position[0] - n_tp[0])
        s_yp = (your_position[1] - n_yp[1])/(your_position[0] - n_yp[0])
        if s_tp == s_yp:
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
    
    if e_dist(your_position, trainer_position) <= distance:
        i = 1
    else:
        i = 0
    
    walls = {'n': dimensions[1], 's': 0, 'e': dimensions[0], 'w': 0}

    e_dist(your_position, s_fold(*w_fold(your_position, trainer_position, walls))[1])
    e_dist(your_position, n_fold(*w_fold(your_position, trainer_position, walls))[1])
    e_dist(your_position, s_fold(*e_fold(your_position, trainer_position, walls))[1])
    e_dist(your_position, n_fold(*e_fold(your_position, trainer_position, walls))[1])
    e_dist(your_position, e_fold(*s_fold(your_position, trainer_position, walls))[1])
    e_dist(your_position, w_fold(*s_fold(your_position, trainer_position, walls))[1])

    e_dist(your_position, n_fold(*w_fold(*s_fold(your_position, trainer_position, walls)))[1])

    return i

# test case
dimensions = [3, 2]
your_position = [1, 1]
trainer_position = [2, 1]
distance = 4