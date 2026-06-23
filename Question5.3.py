# Creating a bytes object
b = b"Hello"

print(b)
print(type(b))



#b[0] = 74#error

arr = bytearray(b"Hello")

print(arr)
print(type(arr))
arr = bytearray(b"Hello")

arr[0] = 74   # ASCII of J

print(arr)