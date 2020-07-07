#####################
##### Solution ######
#####################

def solution(l):
    """
    Approach:

    Step 1: Create a dictionary with i : js key-value pairs, such that for each index i,
            js is a list of the indices j (i < j) for which li divides lj.

    Step 2. Then for each key i, for each j in js, use the dictionary to count the number of
            indices k for which lj divides lk (j < k), and add this count to a running counter.

    The total counter will then be the number of triples (li, lj, lk) such that li divides lj, 
    and lj divides lk (i < j < k).
    """
    # Step 1
    divides_dict = dict()
    for i, li in enumerate(l):
        divides_dict[i] = []
        for j, lj in enumerate(l[i+1:], start=i+1):
            if lj % li == 0:
                divides_dict[i].append(j)

    # Step 2
    counter = 0
    for i, js in divides_dict.items():
        for j in js:
            ks = divides_dict[j]
            counter += len(ks)

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
