from random import random

means = [random() for i in range(10)]
data = [random() for i in range(1000)]

param = 0.01

# O(data*means)
for x in data:
    # O(data)
    closest_k = 0;
    smallest_error = 9999;
    for k in enumerate(means):
        # O(means)
        error = abs(x-k[1])
        if error < smallest_error:
            smallest_error = error
            closest_k = k[0]
        means[closest_k] = means[closest_k]*(1-param) + x*(param)
print (means)
