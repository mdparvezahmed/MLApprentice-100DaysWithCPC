import numpy as np

array = np.array([1,2,3,4])

array = array*2
# print(array)

# print(type(array))
# print(array.ndim)
# print(array.shape)


# array[array<2] = 0
# print(array) 

#integer random number
# rng = np.random.default_rng(seed=1)

# print(rng.integers(low=1, high=101, size=(3,2)))
#floating number
# np.random.seed(seed=1)

# print(np.random.uniform(low=-1,high=1, size=(3,2)))


rng = np.random.default_rng()

# arr = np.array([1,2,3,4,5])

# rng.shuffle(arr)
# print(arr)

fruits = np.array(['apple', 'orragne', 'banana', 'coconut', 'pineapple'])

fruits = np.array(['🍎', '🍊', '🍍','🍌', '🎃', "🍇"])
fruit = rng.choice(fruits, size=(3,3))

print(fruit)
