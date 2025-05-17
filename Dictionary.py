dic ={"a":2, 4:"BB"}

print(dic["a"])

##inserting values into dictionary

dict={ }
dict["fistname"]="Rahul"
dict["gender"]="male"
print(dict)

## for loop
obj=[2,3,5,7,9]
for i in obj:
    print(i)
###### how to iterate through lisy
obj=[2,3,5,7,9]
for i in obj:
    print(i)

##### sum of first natural number 1+2+3
## in js or java we used to give fixed figure to calcualte this but in python
## we  for(i=0, i,5,i++)
summation =0
for j in range(1,6):
    summation = summation + j #range (i,j) -> i to j-1 # (1-5)
print(summation)
#0=+1, 3(2), 6(3),10 (4), 15(5)
print("*******************************")
for k in range(1,10,2): # jump of 2 or increment of 2
    print(k)

    print("**********SKIP First index*********************")
for m in range(10): # In case of no start index the system start from 0 to n-1(9)
    print(m)