#          range                    list
#immutable  yes                      no
#          used less memoey          uesed more memory 


#range 
r=range(5)
r.append(34)#error because range are immutable
print(r)

#list
l=[1,2,3]
l.append(67)
print(l)