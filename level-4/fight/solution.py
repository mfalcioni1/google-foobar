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
    https://plus.maths.org/content/arithmetic-billiards-0
    Combined with this I think there is a concept that can be applied, "unfolding the billiards table"
    with each "fold" (reflection of the table off a given wall) we replace our opponent in space
    then after "x" folds we calculate the distance between us and the folded opponent
    if it is < distance constraint then it is a viable solution.

    This works. I do have to figure out a way to check that you don't hit yourself.
    """
    def dist(p_1, p_2):
        return ((p_2[0] - p_1[0])**2 + (p_2[1] - p_1[1])**2)**0.5
    
    if dist(your_position, trainer_position) <= distance:
        i = 1
    else:
        i = 0
    
    e_wall = [dimensions[0], trainer_position[1]]
    w_wall = [0, trainer_position[1]]
    n_wall = [trainer_position[0], dimensions[1]]
    s_wall = [trainer_position[0], 0]

    def s_fold(yp, tp, e_wall, w_wall, n_wall, s_wall):
        return [tp[0], tp[1] - 2*dist(tp, s_wall)]
    
    def n_fold(tp):
        return [tp[0], tp[1] + 2*dist(tp, n_wall)]
    
    def e_fold(tp):
        return [tp[0] + 2*dist(tp, e_wall), tp[1]]
    
    def w_fold(tp):
        return [tp[0] - 2*dist(tp, w_wall), tp[1]]
    

    dist(your_position, n_fold(trainer_position))

    return i

# test case
dimensions = [3, 2]
your_position = [1, 1]
trainer_position = [2, 1]
distance = 4