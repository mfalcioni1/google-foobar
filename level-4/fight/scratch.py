

x = [1,1]
x_1 = [2.1,1.1]

def dist(p_1, p_2):
    return ((p_2[0] - p_1[0])**2 + (p_2[1] - p_1[1])**2)**0.5

res = dist(x, x_1)
res