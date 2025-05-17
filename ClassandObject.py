## Classes are the uder define blueprint and prototype

class Calculator:
    num=100

    def addData(self):
        print("Im now executing the method in the class")
        #print(addInteger(3, 3))

##creatin object of the class
obj= Calculator()
obj.addData()
print(obj.num)
