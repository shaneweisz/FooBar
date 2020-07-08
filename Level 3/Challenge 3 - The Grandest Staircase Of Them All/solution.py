#####################
##### Solution ######
#####################

def memoize(solve):
    """Applies memoization to `solve(n, k)` to avoid recomputing already-computed results."""
    memo = {}

    def inner(n, k):
        if (n, k) not in memo:
            s_nk = solve(n, k)
            memo[(n, k)] = s_nk
            return s_nk
        return memo[(n, k)]

    return inner


@memoize
def solve(n, k):
    """
    - Returns the number of ways `n` can be made up by summing distinct 
        positive integers with `k` as the biggest integer.
    - This is recursively calculated by summing up the number of ways 
        `n-k` can be be made up with each of `k-1` through to `1` as 
        the biggest integer respectively.
    - For example: 
        solve(7, 4) = solve(3, 3) + solve(3, 2) + solve(3, 1)
                    = 1 + solve(1, 1) + 0
                    = 1 + 1 = 2
        i.e. 7 = 4 + 3      (1)
               = 4 + 2 + 1  (2)
    - Memoization is used to avoid recalculations.
    """
    if n < k:
        return 0
    if n == k:
        return 1
    return sum([solve(n-k, i) for i in range(k-1, 0, -1)])


def solution(n):
    """
    - Returns the number of ways `n` can be made up by summing distinct
        postive integers.
    - This then equals the sum of `solve(n, k)` for `k` running from 1 through to `n-1`
    """
    count = 0
    for k in range(1, n):
        count += solve(n, k)
    return count

#####################
#### Test Cases #####
#####################


inputs = [3, 200]
expected_outputs = [1, 487067745]


def check_test_case(i, inp, exp_out):
    print("-"*20)
    print("Test Case", i)

    out = solution(inp)
    print("Output:", out)
    print("Expected:", exp_out)

    print("PASSED" if out == exp_out else "FAILED")


def run_all_tests(inputs, expected_outputs):
    for i, (inp, exp_out) in enumerate(zip(inputs, expected_outputs), start=1):
        check_test_case(i, inp, exp_out)


run_all_tests(inputs, expected_outputs)
