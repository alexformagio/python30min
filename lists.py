__author__ = 'formagio'
grocery_list = ['bean','rice','beef','salad','tuna','bean','bean']
print("The first element of list is ",grocery_list[0])
print("The second item is ",grocery_list[1])
print("The last item is " ,grocery_list[len(grocery_list)-1])

#changing a value
grocery_list[0]='soup'
print(grocery_list)

#starting at posiion one(second element) of list until thrid elment of list
print(grocery_list[1:3])

#list inside list
other_events=['take a shower','wash dishs','Pick up kids']
to_do_list = [grocery_list,other_events]
print(to_do_list)

for j in to_do_list:
    print('----------------')
    for k in j:
        print(k)


# You add values using append
grocery_list.append('onions')
print(to_do_list)

# Insert item at given index
grocery_list.insert(1, "Pickle")
print(to_do_list)

# Remove item from list
grocery_list.remove("Pickle")
print(to_do_list)

# Sorts items in list
grocery_list.sort()
print(to_do_list)

# Reverse sort items in list
grocery_list.reverse()
print(to_do_list)

# del deletes an item at specified index
del grocery_list[4]
print(to_do_list)

# We can combine lists with a +
to_do_list = other_events + grocery_list
print(to_do_list)

# Get length of list
print(len(to_do_list))

# Get the max item in list
print(max(to_do_list))

# Get the minimum item in list
print(min(to_do_list))

setList = set(grocery_list)
print(grocery_list)
print(setList)