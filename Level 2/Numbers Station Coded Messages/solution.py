#####################
##### Solution ######
#####################

def solution(l, t):
    '''
    * Keep a running sum of the elements starting from l[i]
    * When the sum is >= `t` or the end of the list
        is reached, check if the running sum equals `t`
      If not, move on to the next element of the list, and start
        a running sum from there
    * If none of the running sums equals `t`, then no sub-list can be summed
        to give `t`, so return [-1,-1]
    '''
    n = len(l)

    for i in range(len(l)):

        total = l[i]

        j = i + 1
        while total < t and j < n:
            total += l[j]
            j += 1

        if total == t:
            return [i, j-1]

    return [-1, -1]


#####################
#### Test Cases #####
#####################

inputs = [([1, 2, 3, 4], 15), ([4, 3, 10, 2, 8], 12)]
expected_outputs = [[-1, -1], [2, 3]]


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


run_all_tests(inputs, expected_outputs)
