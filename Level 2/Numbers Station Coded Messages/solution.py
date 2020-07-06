def solution(l, t):
    n = len(l)

    for i in range(len(l)):

        #  * Keep a running sum of the elements starting from l[i]
        #  * When the sum is >= `t` or the end of the list
        #    is reached, check if the running sum equals `t`
        #  * If not, move on to the next element of the list, and start
        #    a running sum from there

        total = l[i]

        j = i + 1
        while total < t and j < n:
            total += l[j]
            j += 1

        if total == t:
            return [i, j-1]

    # If none of the running sums equals `t`, then no sub-list can be summed
    # to give `t`, so return [-1,-1]
    return [-1, -1]


print("-"*20)
print("Test Case 1")
print("Output:", solution([1, 2, 3, 4], 15))
print("Expected: [-1, -1]")
print(solution([1, 2, 3, 4], 15) == [-1, -1])

print("-"*20)
print("Test Case 2")
print("Output:", solution([4, 3, 10, 2, 8], 12))
print("Expected: [2,3]")
print(solution([4, 3, 10, 2, 8], 12) == [2, 3])
print("-"*20)
