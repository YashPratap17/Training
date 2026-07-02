list = []
print(type(list))
list1 = [1,2,3,4,5]
print(list1)
list2 = ["Hi",True,10,10.1]
print(list2)

list3 = [1,2,[3,4,5],6,7,[8,9]]
print(list3)

list.extend(list1)
print(list)

# Accessing of List

print(list[0])
print(list[0:2])

list[2]=10
print(list)

list.extend(list3)
print(list + list2) # Concatenation
print(list*3) # Repetetion

list1.append(6)
print(list1)

list1.insert(5,10)
list1.remove(10) # Takes Value
list1.pop()
print(list1)