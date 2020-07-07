#####################
##### Solution ######
#####################

def solution(x, y):
    x, y = int(x), int(y)
    x, y = min(x, y), max(x, y)  # ensure x <= y

    counter = 0
    while x > 1:
        reduce_factor = y // x
        y -= reduce_factor * x  # repeatedly subtract x from y until y <= x
        x, y = y, x  # swap x and y because now y <= x
        counter += reduce_factor

    if x == 1:
        counter += y - 1
        return str(counter)

    return "impossible"  # since x < 1

#####################
#### Test Cases #####
#####################


inputs = [('4', '7'),
          ('2', '1'),
          ('1000000000', '1'),
          ('1', '1'),
          ('42', '42'), ]

expected_outputs = ["4",
                    "1",
                    str(1000000000 - 1),
                    '0',
                    "impossible", ]


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
