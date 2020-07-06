#####################
##### Solution ######
#####################

def solution(total_lambs):
    return stingy(total_lambs) - generous(total_lambs)


def generous(total_lambs):
    '''
    * Paying LAMBs generously, we get the sequence:
         1, 2, 4, 8, 16, ...

    * For the nth value in the sequence, we have:
         S(n) = 2 ^ n - 1
      where S(n) is the sum of the values of the sequence up to
      and including the nth value

    * We keep adding henchmen until S(n) > total_lambs
    '''

    n = 1

    while 2 ** n - 1 <= total_lambs:
        n += 1

    return n - 1


def memoize(F):
    ''' Applies memoization for an efficient recursive Fibonacci implementation '''
    memo = {}

    def inner(n):
        if n not in memo:
            f_n = F(n)
            memo[n] = f_n
            return f_n
        return memo[n]

    return inner


@memoize
def F(n):
    ''' Returns the nth Fibonacci number '''
    if n == 1:
        return 1
    if n == 2:
        return 1
    return F(n-1) + F(n-2)


def stingy(total_lambs):
    '''
    * Paying LAMBs generously, we get the Fibonacci sequence:
         1, 1, 2, 3, 5, 8, ...

    * For the nth value in the sequence, we have:
         S(n) = F(n + 2) - 1
       where F(n) returns the nth Fibonacci number
       and S(n) returns the sum of first N Fibonacci numbers

    * We keep adding henchmen until S(n) > total_lambs
    '''

    n = 1

    while F(n+2) - 1 <= total_lambs:
        n += 1

    return n - 1


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
