def test(n):
    m = [[0 for i in range(n + 1)] for j in range(n + 1)]
    m[0][0] = 1 
    for steps in range(1, n + 1):
        for prev in range(0, n + 1):
            m[steps][prev] = m[steps - 1][prev]
            if prev >= steps:
                m[steps][prev] += m[steps - 1][prev - steps]
	          	
    return m[n][n] - 1 # drop base case



# Input:
test(200)
# Output:
#    487067745

# Input:
test(3)
# Output:
#    1