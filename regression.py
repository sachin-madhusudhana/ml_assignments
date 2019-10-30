from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
import pdb
import random

## POINTS 
#xs = np.array([1,2,3,4,5,6], dtype = np.float64)
#ys = np.array([5,4,6,5,6,7], dtype = np.float64)


## RANDOM DATASET FOR TESTING
def create_dataset(hm, variance, step=2, correlation=False):
    val = 1
    ys = []
    for i in range(hm):
        y = val + random.randrange(-variance,variance)
        ys.append(y)
        if correlation and correlation == 'pos':
            val += step
        elif correlation and correlation == 'neg':
            val -= step
    xs = [i for i in range(len(ys))]
    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)


## FUNCTION FOR FINDING SLOPE AND INTERCEPT
def best_slope_intercept(xs,ys):
    m =  ((mean(xs) * mean(ys)) - mean(xs*ys)) / ((mean(xs)**2) - mean(xs*xs))
    b = mean(ys) - m * mean(xs)
    return m,b


## SQUARED ERROR 
def squared_error(ys_orig, ys_line):
    return sum((ys_line-ys_orig)**2)


## ERROR DETERMINATION
def coeff_of_determination(ys_orig,ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_reg = squared_error(ys_orig,ys_line)
    squared_error_y_mean = squared_error(ys_orig,y_mean_line)
    return 1-(squared_error_reg/squared_error_y_mean)


xs,ys = create_dataset(40, 30, 2, correlation = 'pos')


m,b = best_slope_intercept(xs,ys)
print(m,b)

regression_line = [m*x+b for x in xs]


r_squared = coeff_of_determination(ys, regression_line)
print(r_squared)


plt.scatter(xs,ys)
plt.plot(xs,regression_line)
plt.show()
