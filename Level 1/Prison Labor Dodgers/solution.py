def solution(x, y):
    # 1. Ensure x is the bigger of the two lists
    #    so that x contains the additional ID
    if len(x) < len(y):
        x, y = y, x

    # 2. Sort the two lists in ascending order
    x.sort()
    y.sort()

    # 3. Compare x_i and y_i where i runs from 1 to n := len(y).
    #    If x_i != y_i, it follows since the lists are sorted
    #    and x contains the additional ID, that x_i must be the
    #    additional ID.
    for x_i, y_i in zip(x, y):
        if x_i != y_i:
            return x_i

    # 4. If x_i = y_i for all i running from 1 to n, then the
    #    (n+1)-th element of x must be the additional ID
    return x_i[-1]


print(solution([13, 5, 6, 2, 5], [5, 2, 5, 13]))
print(solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50]))
