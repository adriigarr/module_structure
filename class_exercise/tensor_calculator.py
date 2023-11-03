# import modules
import torch

class Calculator():
    # all zeros tensor
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

    # multiplication of two tensors
    def mult_tensors(self, tensor1, tensor2):
        mult = torch.matmul(tensor1, tensor2)
        return mult

    # substraction of two tensors
    def resta_tensores(self, tensor1, tensor2):
        rest = tensor1 - tensor2
        return rest

    # division of two tensors
    def division_tensors(self, tensor1, tensor2):
        division = torch.div(tensor1, tensor2)
        return division

    # sum the values of each column of a tensors
    def suma_columnas(self, tensor):
        suma_cols = torch.sum(tensor, dim=0)
        return suma_cols

    # add a value to all the elements of a tensor
    def sumar_valor(self, tensor, value):
        suma_valor = tensor + value
        return suma_valor

    # substract a value to all the elements of a tensor
    def restar_valor(self, tensor, value):
        resta_valor = tensor - value
        return resta_valor

__all__ = ["Calculator"]