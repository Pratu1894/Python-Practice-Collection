#When data type in inmutable (not changable)then>>in case we assigned same value for inmutable data type >>it assigned same id for same data  value or type


var=90
car=90
print(id(var))
print(id(car))
print("\n")
sttrg="pratiksha"
sttrg2="pratiksha"
print(id(sttrg))
print(id(sttrg2))

print("\n")

flag1=True
flag2=True
print(id(flag1))
print(id(flag2))
print("\n")

#incase of mutable data type (changable), id should be different for all data value even if data value is same , still id are different for this bcz it can be  changes once declare 
lst=[10]
lst2=[10]
print(id(lst))
print(id(lst2))