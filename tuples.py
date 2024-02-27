# Tuples in Python
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
# Tuples allow duplicate values.
# Tuples are immutable, which means that you cannot change, add, or remove items after the tuple has been created.

my_tuple = ("francode", "marketer", "SE")
print(my_tuple)

#tuples are ordered

print(my_tuple[1])


# updating a tuple

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# converting a tuple to a list

test_tuple = ("francode", "marketer", "SE")

test_list = list(test_tuple)
test_list[1] = "developer"

test_tuple = tuple(test_list)

print(test_tuple)