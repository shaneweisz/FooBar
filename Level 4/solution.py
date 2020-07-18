#####################
##### Solution ######
#####################

from itertools import permutations


def solution(times, times_limit):
    shortest_paths = floyd(times)
    n = len(times)

    # DETECT NEGATIVE CYCLES
    for i in range(n):
        if shortest_paths[i][i] != 0:
            # Then there is a negative cycle
            return list(range(n-2))

    bunnies = range(1, n-1)
    answer = []
    max_bunnies = 0
    for i in range(1, len(bunnies)+1):
        for p in permutations(bunnies, i):
            time = time_to_collect(p, shortest_paths)
            # print(p, time)
            if time <= times_limit:
                if i > max_bunnies:
                    max_bunnies = i
                    answer = sorted(p)

    return [x - 1 for x in answer]  # change bunny 1 to index 0 etc


def time_to_collect(bunnies_list, shortest_paths):
    """ Returns the amount of time taken to collect the bunnies in
        `bunnies_list` in that order
    """
    first_bunny = bunnies_list[0]
    s = shortest_paths[0][first_bunny]
    for a, b in zip(bunnies_list, bunnies_list[1:]):
        s += shortest_paths[a][b]
    last_bunny = bunnies_list[-1]
    s += shortest_paths[last_bunny][-1]
    return s


def floyd(times):
    shortest_paths = list(times)
    n = len(times)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                shortest_paths[i][j] = min(shortest_paths[i][j],
                                           shortest_paths[i][k] + shortest_paths[k][j])
    return shortest_paths

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
                [9, 3, 2, 2, 0]], 1),
              ([[0, 1, 1, 1, 1],
                [1, 0, 1, 1, 1],
                  [1, 1, 0, 1, 1],
                  [1, 1, 1, 0, 1],
                  [1, 1, 1, 1, 0]], 3)]

    expected_outputs = [[1, 2], [0, 1]]

    run_all_tests(inputs, expected_outputs)


if __name__ == '__main__':
    main()
