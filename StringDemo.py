SLC = "RahulSheltyAcademy.com"  # Fixed: Added quotes for string
str1 = "Consulting firm"
str3 = "RahulShelty"

print(SLC[1])           # Output: "a" (2nd character of SLC)
print(SLC[0:5])         # Output: "Rahul" (substring from index 0-4)
print(SLC + str1)       # Output: "RahulSheltyAcademy.comConsulting firm"
print(str3 in SLC)      # Output: True ("RahulShelty" is part of SLC)
var= SLC.split(".")
print(var)

str4 = " great "
print(str4.strip())   # Output: "great" (removes leading/trailing spaces)
print(str4.lstrip())  # Output: "great " (removes left/leading space only)
print(str4.rstrip())  # Output: " great" (removes right/trailing space only)