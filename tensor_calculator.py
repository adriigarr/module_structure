# import modules
import torch


class Calculator():

    def __init__(self):
        return None
    
    # all zeros ensor
    def all_zeros(self, dim_x, dim_y):
        zeros = torch.zeros(dim_x, dim_y)
        return zeros
    
    # all ones tensors
    def all_ones(self, dim_x, dim_y):
        ones = torch.ones(dim_x, dim_y)
        return ones
    
    # tensor with random values
    def all_rand(self, dim_x, dim_y):
        random_num = torch.rand(dim_x, dim_y)
        return random_num

    # sum of two tensors
    def sum_tensors(self, tensor1, tensor2):
        suma = tensor1 + tensor2
        return suma

    def mult_tensors(self, tensor1, tensor2):
        mult = torch.matmul(tensor1, tensor2)
        return mult

    def resta_tensores(self, tensor1, tensor2):
        rest = tensor1 - tensor2
        return rest

arr1 = [1,2,3,4]
arr2 = [2, 4, 6, 8]
tupla_dim = (2, 2)

# funcion para pasar los arrays de datos a tensores, teniendo en cuenta la deseada dimension
def create_tensor(arr, dimension):
    a = torch.tensor(arr).view(dimension)
    return a

t1 = create_tensor(arr1, tupla_dim)
t2 = create_tensor(arr2, tupla_dim)

