#input function always written str ,  bcz it accepts input as text
#we can convert this into another data type using type casting 
print("Enter value")
value=input()#it will defult accept any value as str
print(type(value))

print("\n")
#type casting using two ways 1)at time of accepting, 2)after accepting int(var)
#1) at time of accepting 
print("Enter number ")
no=int(input())
print(type(no))
print("\n")

#2)after accepting 
print("enter value 2")
no2=input()
int(no)
print(type(no))
