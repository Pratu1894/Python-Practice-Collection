#                   List                             Tuple 
#---------------------------------------------------------------------
#Mutability        | Mutable (can be changed)       | Immutable (cannot be changed)
#Memory Usage     | More memory usage              | Less memory usage
#Performance       | Slower due to mutability       | Faster due to immutability
#Use Cases        | Suitable for collections that | Suitable for fixed collections
#                  | may change over time           | that should not change

from sys import getsizeof
#list mutable 
lst=[11,12,13,14]
print(lst)
lst[1]=34
print(lst)


#tuples are immutable 
tup=(11,12,13,14)
print(tup)
#lst1[1]=34#error
print(tup)

print(getsizeof(lst))#list contains more memory size than tuples
print(getsizeof(tup))

