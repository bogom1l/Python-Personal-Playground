import numpy as np

# list_two = list(range(1, 4))
# list_three = list(range(1, 4))
# list_sum = []
#
# print(list_two)
# print(list_three)
#
# for i in range(3):
#     list_two[i] = list_two[i] ** 2
#     list_three[i] = list_three[i] ** 3
#     list_sum.append((list_two[i] + list_three[i]))
#
# print("After:")
# print(list_two)
# print(list_three)
# print(list_sum)

# array1 = np.arange(1, 4)
# print(array1)
#
# array2 = np.arange(1, 4) ** 2
# print(array2)
#
# array3 = np.arange(1, 4) ** 3
# print(array3)
#
# print(array2 + array3)

# sample_array = np.array([1, 2, 3])
#
# arr = np.power(sample_array, 4)
# print(arr)
#
# arr2 = np.negative(sample_array)
# print(arr2)
#
# print(np.exp(sample_array))
#
# print(np.log(sample_array))


##-------- Multidimensional arrays --------

# x = np.arange(3)
# y = np.arange(3)
# z = np.arange(3)
#
# multi_array = np.array([x, y, z])
# print(multi_array)
# print(multi_array.shape)
#
# w = np.linspace(0, 20, 11, False)
# print(w)
#
# b = np.arange(1, 30, 3)
# print(b)


# x = np.arange(3)
# y = np.arange(3, 6)
# z = np.arange(6, 9)
#
# multi_array = np.array([x, y, z])
# print(multi_array)
#
# print(multi_array[0, 0])
# print(multi_array[1, 2])
#
# print(multi_array.dtype)


# ~~~~~~~~~~~~~~~~~~~~~~~~ simple exercises ~~~~~~~~~~~~~~~~~~~~~~~~

# # 1.Create a 3x3 matrix with values ranging from 1 to 9
# matrix = np.arange(1, 10).reshape(3, 3)
# print(matrix)
#
# # 2.Given matrix, extract the second column
# matrix = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])
#
# second_column = matrix[:, 1]
# print(second_column)

# ~~~~~~~~~~~~~~~~~~~~~~~~


# ==== Slicing ====

# x = np.arange(1, 10)
#
# print(x[2:7])
# print(x[2:7:2])
# print(x[:7])
# print(x[2:])

# x = np.arange(9)
# print(x)
# print("-----------------")
#
# x = np.arange(9).reshape(3, 3)
# print(x)
# print("-----------------")
#
# x = np.arange(9).reshape(3, -1)
# print(x)
# print("-----------------")
#
# x = np.arange(18).reshape(2, 3, 3)
# print(x)
# print("-----------------")
#
# x = np.arange(18).reshape(3, 3, 2)
# print(x)
# print("-----------------")

#---------------------------------------------------------

# x = np.arange(18).reshape(3, 2, 3)
# print(x)
# print(x[1, 1, 1])
#
# print(x[1, 0:2, 0:3])
# print(x[1, :2, :3])
# print(x[1, :, :])
# print(x[1, ...])
# print("------------")
#
# print(x[:, 0, 0])
# print("------------")
#
# print(x[1, :2, :3])
# print(x[1, :2, :3:2]) #each second element
# print("------------")
#
# comparison_operation = x > 4
# print(comparison_operation)
# print(x[comparison_operation])
# print(x[x > 4])
# print(x.max())
# print(x.min())


# Manipulating Array Shapes

# x = np.arange(9).reshape(3, 3)
# print(x)
#
# ravelled_array = x.ravel()  # from 2D array to 1D array | returns view (the original array)
# ravelled_array[2] = 123
# print(ravelled_array)
# print(x)
# print("-----------------------------")
#
# x = np.arange(9).reshape(3, 3)
# print(x)
# print("-----------------------------")
#
# flattened_array = x.flatten()  # from 2D array to 1D array | returns copy
# flattened_array[1] = 123
# print(flattened_array)
# print(x)
# print("-----------------------------")

# y = np.arange(9)
# y.shape = [3, 3]
# print(y)
# print("-----------------------------")
#
# print(y.transpose())
# print(y.T)
# print("-----------------------------")
#
# print(np.resize(y, (6, 6)))
# print("-----------------------------")
#
# print(np.zeros((6,), dtype=int))
# print("-----------------------------")
#
# print(np.ones((6,), dtype=int))
# print("-----------------------------")
#
# print(np.eye(5, dtype=int))
#
# print(np.random.rand(4, 4))


# Matrix Multiplication

# matrix_a = np.matrix([0, 3, 5, 5, 5, 2]).reshape(2, 3)
# print(matrix_a)
#
# matrix_b = np.matrix([3, 4, 3, -2, 4, -2]).reshape(3, 2)
# print(matrix_b)
#
# matrix_sum = matrix_a * matrix_b
# print(matrix_sum)


# Stacking

# x = np.arange(4).reshape(2, 2)
# print(x)
#
# y = np.arange(4, 8).reshape(2, 2)
# print(y)
#
# z = np.hstack([x, y])
# print(z)
# print(z.shape)
# print("----------------------------------------")
#
# v = np.arange(4).reshape(2, 2)
# print(v)
#
# b = np.arange(8).reshape(4, 2)
# print(b)
#
# n = np.vstack([v, b])
# print(n)
# print(n.shape)
# print("----------------------------------------")
#
# w = np.concatenate((x, y), axis=0)
# print(w)
# print("----------------------------------------")


# Depth Stacking

# x = np.arange(4).reshape(2, 2)
# print(x)
#
# y = x * 2
# print(y)
# print("----------------------------------------")
#
# depth_stack = np.dstack((x, y))
# print(depth_stack)
# print(depth_stack.shape)


# x = np.arange(4).reshape(2, 2, 1)
# print(x)
#
# y = x * 2
# print(y)
# print("----------------------------------------")
#
# depth_stack = np.dstack((x, y))
# print(depth_stack)
# print(depth_stack.shape)


# Column Stacking

x = np.arange(4).reshape(2, 2)
print(x)

y = x * 2
print(y)
print("----------------------------------------")

column_stacking = np.column_stack((x, y))
print(column_stacking)
print(column_stacking.shape)
print(column_stacking == np.hstack((x, y)))

