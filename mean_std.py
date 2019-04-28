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
print(np.mean(nplist,axis=1))
print(np.var(nplist,axis=0))
print(round(np.std(nplist,axis=None),11))