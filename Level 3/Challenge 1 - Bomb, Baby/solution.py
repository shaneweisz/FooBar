#####################
##### Solution ######
#####################

def solution(x, y):
    x, y = int(x), int(y)

    # 1. The solution will be symmetric, so ensure x <= y
    x, y = min(x, y), max(x, y)

    counter = 0
    while x >= 1 and y > 1:
        if y % x != 0:
            n = (y // x)
        elif x == 1:
            n = (y // x) - 1
        else:
            return "impossible"
        y -= n * x
        # swap x and y because now y <= x
        x, y = y, x
        counter += n

    possible = x == 1 and y == 1

    return str(counter) if possible else "impossible"

#####################
#### Test Cases #####
#####################


n = 10000000000000000000
inputs = [('4', '7'), ('2', '1')] + [(str(n), '1')] + \
    [('1', '1')] + [('42', '42')]
expected_outputs = ["4", "1"] + [str(n - 1)] + ['0'] + ["impossible"]


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
