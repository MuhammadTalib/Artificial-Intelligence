import numpy as np

#a=np.array([[1, 2], [3, 4],[5,6]])
#print(a.ndim)
#print(np.min(a,axis=1))
#print(np.min(a,axis=0))
#print(np.min(a,axis=None))

#print(np.max(a,axis=1))
#print(np.max(a,axis=0))
#print(np.min(a,axis=None))

import numpy as np 

arr=input()
arr=arr.split(" ")                                              
N = int(arr[0])
M = int(arr[1]) 
list=[] 
for i in range(N): 
  arr = input()
  arr=arr.split(" ")
  arr2=[]
  for j in arr: 
    arr2.append(int(j))
  list.append(arr2)
                                
nplist=np.array(list)
min_axis1=np.min(nplist,axis=1)
print(np.max(min_axis1))


