#sets are used to store multiple items in a single variable.
# A set is a collection which is both unordered and unindexed.
# Sets are written with curly brackets.
# NO duplicates of items are allowed in a set.


# let's Create a Set:


my_set = {"Francode", "Python", "DJango", "HTML", "CSS", "Javascript"}

print(my_set)
print(len(my_set)) # length of the set
print(type(my_set)) # type of the set


# testing duplicates

test_set = {True, False, 1, 0}
print(test_set)

#using the set constructor to create a set

new_set = set(("Francode", "Python", "DJango", "HTML", "CSS", "Javascript")) # No usage of curly brackets

print(new_set)
