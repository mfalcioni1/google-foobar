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

    The distance of the ball from the rail being targeted
    to the target ball creates similiar triangles
    if they are equidistant from the rails then the triangles are congruent

    I believe the net result is that each carom produces a new either
    similiar or congruent triangle of which we need to calculate the one side
    of to see if it violates the distance constraint. Then we need to find
    the carom counting pattern. i.e. 1 carom not on the same x or y produces
    4 possible solutions (2 pairs of symmetric solutions), 
    whereas equal y or x limits it to two.
    """
    def dist(p_1, p_2):
        return ((p_2[0] - p_1[0])**2 + (p_2[1] - p_1[1])**2)**0.5
    
    if dist(your_position, trainer_position) <= distance:
        i = 1
    else:
        i = 0

    # find max bounces
    

    return i

