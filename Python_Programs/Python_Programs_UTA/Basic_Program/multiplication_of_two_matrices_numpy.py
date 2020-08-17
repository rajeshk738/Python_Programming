
def product_of_two_matrices(a,b):
    import numpy
    product = (numpy.mat(a) * numpy.mat(b))
    product_to_list = product.tolist()
    return product_to_list


a = [[2, 3, 4],
     [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]

print(product_of_two_matrices(a,b))
