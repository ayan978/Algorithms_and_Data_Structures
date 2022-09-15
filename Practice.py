
import numpy as np

arr1 = np.empty(6,int)

def func1():
    arr1[0] = 10
    print(arr1[0])

def func2():
    arr1[1] = 15
    print(arr1)

func1()
func2()