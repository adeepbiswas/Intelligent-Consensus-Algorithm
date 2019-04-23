from matplotlib import pyplot as plt
from pandas import read_csv

cv = read_csv('countervalues.csv', header=None)
x=cv.values.tolist()
y=[]

i=50
while i<1050:
    y.append(i)
    i = i + 50
print(x)
plt.plot(y, x)
plt.title("Counter Value Analysis Results")
plt.ylabel("Counter Values")
plt.xlabel("Number of Nodes in the network")
plt.show()