#####################
##### Solution ######
#####################
def solution(total_lambs):
    return stingy(total_lambs) - generous(total_lambs)


def generous(total_lambs):

    i = 1
    t = 1
    v = 2
    while t + v <= total_lambs:
        t += v
        v *= 2
        i += 1

    return i


def stingy(total_lambs):
    a = 1
    b = 1

    i = 1
    t = a
    while t + b <= total_lambs:
        t += b
        a, b = b, a+b
        i += 1

    return i

#####################
#### Test Cases #####
#####################


inputs = [143, 10]
expected_outputs = [3, 1]


def check_test_case(i, inp, exp_out):
    print("-"*20)
    print("Test Case", i)

    out = solution(inp)
    print("Output:", out)
    print("Expected:", exp_out)

    print("PASSED" if out == exp_out else "FAILED")


for i, (inp, exp_out) in enumerate(zip(inputs, expected_outputs), start=1):
    check_test_case(i, inp, exp_out)
