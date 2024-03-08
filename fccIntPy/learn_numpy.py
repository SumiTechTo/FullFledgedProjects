import numpy as np
import sys
import time
print(sys.version)
a=np.array([1,2,3])
print(a)

l=range(1000)
print(sys.getsizeof(1)*len(l))  
# getsizeof gets the size of the given index in bytes

array=np.arange(1000)

print(array.size)
# total size of array

print(array.itemsize)
# size of one array element in bytes

print(array.size*array.itemsize)

# each python list element takes 28 bytes but nnumpy takes native size of the data type and so uses 
# less memory  

size = 1000000

l1= range(size)
l2=range(size)

a1=np.arange(size)
a2=np.arange(size)

start=time.time()

result= [(x+y) for x,y in zip(l1,l2)]

print("python list took", (time.time()-start)*1000)

start=time.time()

result= a1+a2
#convenient

print("Numpy took", (time.time()-start)*1000)

arr=np.array([[1,2],[3,4],[5,7]])
print(arr.ndim)
# gives dimension

print(arr.dtype)
# gives datatype

print(arr.size)
#gives the total no.of elements,here =6


#output -> (no.of rows,columns)
arr.reshape(2,3)
print(arr)

arr=np.array([[1,2],[3,4],[5,7]], dtype=complex)
print(arr)
#type castng the array

arra=np.zeros((5,2))
print(arra)

arra=np.arange(1,8)
print(arra) #excludes the last digit ,here=[1 2 3 4 5 6 7]

arra=np.arange(1,5,2)
print(arra)
# [1 3]

arra=np.linspace(1,7,10)
# generates 10 no. between 1 and 7
print(arra) 

# to make an array one dimensional 
arr1=arr.ravel()
print(arr1)
print("-------")
#doesnt change the original array

for ceel in arr.ravel():
    print(ceel)


#maths with numpy

print(arr1.min())
print(arr1.max())
print(arr1.sum())

#axes in numpy

# axis0= column
# axis 1 =row
print(arr.sum(axis=0))
# sum of row 0, sum on row 1, sum of row n 

print(np.sqrt(arr))

print(np.std(arr))
#gives standard deviation


a=np.array([[1,2],[3,4],[5,6]])
b=np.array([[6,7],[8,10],[5,14]])
#arrays must be of same shape

print(a+b)

print(a-b)

print(a*b)

print(a/b)

# print(a.dot(b))
#gives matrix multiplication


#####Indexing

a=np.array([6,7,8])

print(a[0:2])

a=np.array([[6,7,8],[1,2,3],[6,8,5]])
b=np.array([[6,7,8],[1,2,3],[6,8,5]])


print(a[0:2,2])
# goes through rows 0 to 1 and prints the 2nd indexed element here=[8 3]

print(a[-1])
#gives the last row

print(a[-1,0:2])
# print(var[row,start_range:end_range])


# for all the rows just use colon
print(a[:,0:2])

####Iterating throug array

for row in a:
    print(row)

for cell in a.flat:
    print(cell)
# flattens the array and so we can iterate all through it


####stacking
print(np.vstack((a,b)))

print(np.hstack((a,b)))

a=np.arange(12).reshape(3, 4)
print(a)

c=a>5
print(c)

#prints the element with True
print(a[c])

a[c]=1
print(a)


###nditer funtion

for x in np.nditer(a,order="c"):
    print(x)
    # c===left to right
    #f===up=down