import numpy as np
arr = np.array([10,20,30,40,50,60,70])
print(arr[1:6:2])

import numpy as np
def array(arr):
    arr=np.array(arr,int)
    return arr.reshape(3,3)
arr=input().strip().split(" ")
p=array(arr)
print(p)