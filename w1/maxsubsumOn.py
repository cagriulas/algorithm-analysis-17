def maxsubsumOn(vector):
    max_ending_here = max_so_far = vector[0]
    for x in vector[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

array=[4,-3,15,-2,-1,2,-6,2]
print(maxsubsumOn(array))
