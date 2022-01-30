def solution(num_buns, num_required):
    """
    total keys = num_buns choose num_required
    each key must be possessed num_required times
    This means each rabbit must hold (total_key*num_required)/num_buns keys
    """