#####################
##### Solution ######
#####################
from collections import defaultdict


def solution(l):

    divides_dict = dict()

    for i, li in enumerate(l):
        divides_dict[i] = []
        for j in range(i+1, len(l)):
            lj = l[j]
            if lj % li == 0:
                divides_dict[i].append(j)

    counter = 0
    for k, vs in divides_dict.items():
        for v in vs:
            counter += len(divides_dict.get(v))

    return counter

#####################
#### Test Cases #####
#####################


inputs = [[1, 1, 1], [1, 2, 3, 4, 5, 6]]
expected_outputs = [1, 3]


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
