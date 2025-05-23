file = open('textfile.txt')

#print(file.read(5))
#print(file.readline())

#print line by line using readline method

#line = file.readline()
#while line != "":
 #   print(line)
#    line = file.readline()


 # Example 2: Using readlines() in a for loop

    #values = ["abc", "bvdsf", "cat", "dog", "elephant"
for line in file.readlines():  # Read all lines into a list
    print(line)  # Clean up newline characters

file.close()
