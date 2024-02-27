# dictionaries store data values in keys and value pairs
# A dictionary is a collection which is unordered, changeable and indexed. 
# In Python dictionaries are written with curly brackets


# example dictionary

# my_dict = {"name": "francode", "job": "marketer", "title": "SE"}

# print(my_dict)

# #accesing items in a dictionary

# Test_dict = {"name": "James", "job": "marketer", "title": "ME"}

# y = Test_dict["job"]
# print(y)

# #using the get method

# x = Test_dict.get("name")
# print(x)

# # obtaining the keys from adictionary using the get method

# z = Test_dict.keys()
# print(z)

# # updating items in a dictionary

# my_dict["job"] = "developer"

# print(my_dict)

# # checking is items exist in a dictionary

# if "name" in my_dict:
#     print("Yes, name is one of the keys in the dictionary")
# else:
#     print("No, name is not one of the keys in the dictionary")


#dictionary manipulatio

# # adding items to a dictionary

my_dict = {"name": "francode", "job": "marketer", "title": "SE"}

my_dict["age"] = 25

print(my_dict)

# removing items from a dictionary

my_dict.pop("age")
print(my_dict)

# looping through a dictionary

for x in my_dict:
    if x == "name":
        print("Yes, name is one of the keys in the dictionary")
    print(x)
for x in my_dict.values():
    print(x)

for x in my_dict.keys():
    print(x)

for x in my_dict.items():
    print(x)

#duplicating a dictionary
    
my_dict2 = my_dict.copy()

print(my_dict2)
