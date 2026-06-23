x=10
y=10
print(id(x))
print(id(y))
#python manages memory automatically 
# both are having same id , both are stored in same memory location just beacuse both variables are having same value and they are immutable data type. so python is optimizing memory by storing only one copy of the value and both variables are pointing to that memory location. this is called interning in python.


n=10
n=70#automatically removes the 10 from memory 
