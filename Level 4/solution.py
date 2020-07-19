#####################
##### Solution ######
#####################

from itertools import permutations


def solution(times, times_limit):
    num_vertices = len(times)

    # 1. Compute the shortest paths between any vertex and any
    #    other vertex using Floyd-Warshall

    shortest_paths = floyd_warshall(times)

    # 2. Check for a negative cycle. If there is a negative cycle,
    #    all the bunnies can be collected since as much time as needed
    #    can be gained by repeatedly traversing this cycle

    if is_negative_cycle(shortest_paths):
        num_bunnies = num_vertices - 2  # excluding the start and bulkhead
        all_bunnies = list(range(num_bunnies))
        return all_bunnies

    # 3. Enumerate the possible permutations of bunnies that can be collected.
    #    evaluating the least time needed to collect each permutation of bunnies
    #    in that order, and storing the permutation that collects the most bunnies
    #    but satisfies the time constraint.

    first_bunny = 1
    last_bunny = num_vertices - 2
    bunnies = range(first_bunny, last_bunny + 1)

    answer = []
    max_bunnies = 0
    for perm_size in range(1, len(bunnies)+1):
        for bunnies_perm in permutations(bunnies, perm_size):
            time_taken = least_time_to_collect(bunnies_perm, shortest_paths)

            if time_taken <= times_limit and perm_size > max_bunnies:
                max_bunnies = perm_size
                answer = sorted(bunnies_perm)

    # Adjustment for vertex i corresponding to bunny i - 1
    return [x - 1 for x in answer]  # change bunny 1 to index 0 etc


def floyd_warshall(times):
    """
    Applies the Floyd-Warshall algorithm to computes a matrix with the time 
    taken on the shortest paths between any vertex and any other vertex.
    """
    shortest_paths = list(times)  # make a copy of times
    num_vertices = len(times)

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                shortest_paths[i][j] = min(shortest_paths[i][j],
                                           shortest_paths[i][k] + shortest_paths[k][j])

    return shortest_paths


def is_negative_cycle(shortest_paths):
    """
    Returns True if there is a path from a vertex to itself 
    that takes negative time, else returns False.
    """
    n = len(shortest_paths)
    for i in range(n):
        if shortest_paths[i][i] < 0:  # Then there is a negative cycle
            return True
    return False


def least_time_to_collect(bunnies, shortest_paths):
    """ 
    Returns the least amount of time needed to collect the bunnies in
    `bunnies` in the given order, using the `shortest_paths` matrix.

    e.g. if `bunnies = [1, 3, 4]`, then this returns the least time needed to 
    collect the bunny at vertex 1 (starting at vertex 0), then the one at 
    vertex 3, and finallly the bunny at vertex 4, before returning to the bulkhead.
    """
    # Path from start to first bunny
    start = 0
    first_bunny = bunnies[0]
    time_taken = shortest_paths[start][first_bunny]

    # Successive paths from first bunny through to last bunny
    for curr_bunny, next_bunny in zip(bunnies, bunnies[1:]):
        time_taken += shortest_paths[curr_bunny][next_bunny]

    # Path from last bunny to bulkhead
    bulkhead = -1
    last_bunny = bunnies[-1]
    time_taken += shortest_paths[last_bunny][bulkhead]

    return time_taken


#####################
#### Test Cases #####
#####################


def check_test_case(i, inp, exp_out):
    print("-"*20)
    print("Test Case", i)

    out = solution(*inp)
    print("Output:", out)
    print("Expected:", exp_out)

    print("PASSED" if out == exp_out else "FAILED")


def run_all_tests(inputs, expected_outputs):
    for i, (inp, exp_out) in enumerate(zip(inputs, expected_outputs), start=1):
        check_test_case(i, inp, exp_out)


def main():
    inputs = [([[0, 2, 2, 2, -1],
                [9, 0, 2, 2, -1],
                [9, 3, 0, 2, -1],
                [9, 3, 2, 0, -1],
                [9, 3, 2, 2,  0]], 1),

              ([[0, 1, 1, 1, 1],
                [1, 0, 1, 1, 1],
                [1, 1, 0, 1, 1],
                [1, 1, 1, 0, 1],
                [1, 1, 1, 1, 0]], 3)]

    expected_outputs = [[1, 2], [0, 1]]

    run_all_tests(inputs, expected_outputs)


if __name__ == '__main__':
    main()
