"""Given a list of integers, find the nearest pair
that sum to a given target.
Nearest refers to the positions in the list"""

elements = [1, 5, 3, 6, 4, 2]
target = 7


def _partial_solution(elements, idx0, distance_between_idx, target):
    """Starting from idx0, returns the idx1, such that
    elements[idx0]+elements[idx1]==target

    returns none if the solution does not exist

    distance_between_idx is the maximum acceptable distance
     (so you can discard solutions worse than those already found)"""

    n = len(elements)
    idx1 = idx0 + 1

    while (idx1 - idx0 < distance_between_idx) and (idx1 < n):
        cond = (elements[idx0] + elements[idx1]) == target
        if cond:
            return idx1
        else:
            idx1 = idx1 + 1
    return None


def idx_sum_is(elements, target):
    n = len(elements)
    idx_solution=(None, None)
    for idx0 in range(n - 1):
        idx1 = _partial_solution(elements, idx0, 1, target)
        if idx1 is not None:

            """A possible solution. It is better that the previous one.
            But we need to look for better solutions. """
            idx_solution = (idx0, idx1)
            distance_between_idx = idx1 - idx0
            if distance_between_idx == 1:
                # no better solutions is possible
                return idx_solution
    return idx_solution