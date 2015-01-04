__author__ = 'formagio'
# TUPLES -------------
# Values in a tuple can't change like lists

pi_tuple = (3, 1, 4, 1, 5, 9)
string_tuple = ("alexandre","Thais","Mariana","Evelyn")

print("pi_tuple has %d elements" % len(pi_tuple))
for t in pi_tuple:
    print(t)

print("string_tuple has %d elements" % len(string_tuple))
for name in string_tuple:
    print(name)

# Convert tuple into a list
new_tuple = list(pi_tuple)

# Convert a list into a tuple
# new_list = tuple(grocery_list)

# tuples also have len(tuple), min(tuple) and max(tuple)