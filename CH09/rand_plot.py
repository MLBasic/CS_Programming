import matplotlib.pyplot as plt
import random

numbers = []
for i in range(10):
    numbers.append(random.randint(1,10))

plt.plot(numbers)
plt.ylabel('Some Random Numbers')
plt.show()
