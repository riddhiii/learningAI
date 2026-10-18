import numpy as np
marks=np.array([85, 90, 78, 92, 88])
print(marks+5)
print(marks.shape)
mar=np.array([[90,89,79],[90,89,90]])
print(mar.shape)

# aggregate functions

array=np.array([[1,2,3,4,5],
                [6,7,8,9,10]])
print(np.sum(array))
print(np.mean(array))



#linear regression
x=np.array([1,2,3,4])
y=np.array([5,6,7,8])

m=10
c=5
predictions= m*x+c
errors = y= -predictions
mse= np.mean(errors**2)
print("predictions:",predictions)
print("Errors: ",errors)
print("mse:",mse)


#gradient
import numpy as np

x = np.array([1, 2, 3], dtype=float)
y = np.array([10, 20, 30], dtype=float)

m = 5.0
c = 0.0
learning_rate = 0.01


predictions = m * x + c


dm = (2 / len(x)) * np.sum((predictions - y) * x)
dc = (2 / len(x)) * np.sum(predictions - y)


m = m - learning_rate * dm
c = c - learning_rate * dc

print("New weight:", m)
print("New bias:", c)