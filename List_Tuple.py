  ## You can pass differnt data type in list of python

## Object name (Values)
values =[1,2,"rahul",4,5]

print(values[0]) # 1 output

print(values[3 ]) # 4 output

print(values[-1]) # 5 output

print(values[1:3]) # 2 , rahul,4 ioutput

values.insert(3,"Majeed")
print(values)

##add any value to the end of the list
values.append("End")
print(values)

## Replace/update  any value at any index
values[2]= "BISMAL"
print(values)

## delete
del values[0]
print(values)

## You cannot change update in the tuple (Immutable= means data is protected in tuple)
## data in a tuple is written using parenthesis and commas

val: tuple[int, int, int, str] = (10,9,3,"bismal")
print(val[1])

## Dictionary
dic = {"a":2, 4:"abdc","c":"Hello World"}

