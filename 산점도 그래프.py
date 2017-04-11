
import matplotlib.pyplot as plt
from random import shuffle

xs =[x+1 for x in range(100)]
ys=[y+1 for y in range(100)]

shuffle(xs)
shuffle(ys)

plt.scatter(xs, ys, label='samples', color='c' , marker='o')
plt.show()
