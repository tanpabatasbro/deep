data_0 = [1,2]
data_1 = [3,4]
data_2D = [data_0,data_1]
data_2D_copy = data_2D.copy() 
print(f"data = {data_2D}")
print(f"data = {data_2D_copy}")

#mengambil data list
data =  data_2D[1][0]
print(f"data = {data}")

#adrees data 2D
print(f"adrees asli = {hex(id(data_2D))}")
print(f"adrees copy = {hex(id(data_2D_copy))}")

print(10*"=","adrees dari member ke-1",10*"=")
print(f"adrees asli = {hex(id(data_2D[0]))}")
print(f"adrees copy = {hex(id(data_2D_copy[0]))}")
print("#"*50)
#deep copy
from copy import deepcopy

data_2D = [data_0,data_1]
data_2D_deepcopy = deepcopy(data_2D)

print(f"adrees asli = {hex(id(data_2D))}")
print(f"adrees deep copy = {hex(id(data_2D_deepcopy))}")
print(10*"=","adrees dari member ke-1",10*"=")
print(f"adrees asli = {hex(id(data_2D[0]))}")
print(f"adrees copy = {hex(id(data_2D_deepcopy[0]))}")

print("#"*50)
data_2D[1][0] = 50
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
print(f"data deep = {data_2D_deepcopy}")
