import matplotlib.pyplot as plt
import random

vector = []

for i in range(100):
    rand_number = random.randrange(0, 5, 1)
    vector.append(rand_number)
    
plt.boxplot(vector)
plt.title("BoxPlot")
plt.show()