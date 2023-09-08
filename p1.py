import numpy as np 
array1 = np.random.randint(10,50,size=(5,5))
print(array1)

array1[array1 % 2 != 0] = -1
#print(new_array)
'''for i in array1:
	print(i)
	if i % 2 == 0:
		i=-1
	else :
		i  '''

print(array1)