### While loop depend on condition
it = 4

while it>1:
    if it != 3:
        print(it)
    it= it -1


print("While loop execution is done")

#### Break usage
it = 4
while it>1:
    if it == 3:
        break
    print(it)
    it= it -1
print("While loop execution is break ")

#### continue  usage
it = 10
while it>1:
    if it == 9:
        it = it- 1
        continue ## skip the next iterations
    if it == 3:
        break
    print(it)
    it= it -1
print("While loop execution is continue ")