# Module Structure

This repository contains projects in order to understand the basics of Machine Learning.
The file "class_exercise" contains the first exercise of the course which is a Calculator for operations with tensors. 

## Table of contents
1. Tensor Calculator Exercise
2. How to use the Calculator
3. Example 


### Tensor Calculator Exercise

In this exercise the main target was to do some operation with two dimensional tensors using Pytorch. 
We should be able to do some basic calculations such as:
- all_zeros: function to return an all-zeros tensor
- all_ones: function to return an all-ones tensor
- all_rand: function to return a tensor with random numbers
- sum_tensor: funtion that returns the sum of two tensors
- mult_tensor: functin that returns the multiplication of two tensors

I have created some additional functions such as. 
This functions are:
- resta_tensores: function that returns the substraction of two tensors
- division_tensors: function that returns the division of two tensors
- suma_columnas: function that returns a tensor with the sum of the values of each column
- sumar_valor: function that returns a tensor where a value has been added to all the elements
- restar_valor: function that returns a tensor where a value has been substracted to all the elements in the tensor


### How to use the Calculator
In this section I am going to provide a set of instructions in order to try out the module. 
1. In a jupyter, vscode terminal or pycharm terminal, install the module with the next command
   pip install -U git+https://github.com/adriigarr/module_structure.git
2. Once you have succesfully installed the module, you have to import the library with the next line of code:
    from class_exercise.tensor_calculator import *
3. Once you have imported the library, you can start calling the different functions. In order to do this first you'll have to create a new object of the class. 
   instance = Calculator()
4. When you have done all of this, you are able to try out all the functions. 
   instance.all_zeros(dimx, dimy) 

Before showing an example, here you will find the list of the different functions and how to implement them.m
- instance.all_zeros(dimx, dimy) 
- instance.all_ones(dimx, dimy)
- instance.all_rand(dimx, dimy)
- instance.sum_tensors(tensor1, tensor2)
- instance.mult_tensors(tensor1, tensor2)
- instance.resta_tensores(tensor1, tensor2)
- instance.division_tensors(tensor1, tensor2)
- instance.suma_columnas(tensor)
- instance.suma_valor(tensor, value)
- instance.resta_valor(tensor, value)

### Example
Here is an example with jupyter notebook. 
1. Install the module
2. ```bash
   pip install
   
   ```
![](../../../var/folders/j0/jds78ygj6jn1fjs_9pzdj34c0000gn/T/TemporaryItems/NSIRD_screencaptureui_NNv53u/Screenshot 2023-11-03 at 16.36.18.png)
2. Import the module
![](../Downloads/WhatsApp Image 2023-11-03 at 16.28.06.jpeg)
3. Create new instance for the class
![](../Downloads/WhatsApp Image 2023-11-03 at 16.28.58.jpeg)
4. Create the tensors
![](../Downloads/WhatsApp Image 2023-11-03 at 16.31.21.jpeg)
5. Execute the function
![](../Downloads/WhatsApp Image 2023-11-03 at 16.31.50.jpeg)
