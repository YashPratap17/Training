print("Hello World!")

b = True
print(type(b))

a = True
b = False
print(a + b)

s1 = 'yashpratapsingh'
print(type(s1))
print(s1[0:4])
print(s1[4:10])
print(s1[10:])
print(s1[::-1])

print(int(516.21))
print(int(True))
print(int(False))
print(int("100"))

print(float(5))
print(float(516.21))
print(float(True))
print(float(False))
print(float("3.14"))

print(bool(0))
print(bool("False"))
print(bool(0.0))
print(bool(0+0j))
print(bool(5))
print(bool("True"))
print(bool(5.5))
print(bool(5+5j))
print(bool("Hi"))

print(complex(5))
print(complex(5.5))
print(complex(True))
print(complex(False))

l1 = [1, 2, 3, "four"]
print(type(l1))
print(l1[0])
l1.append(5)
print(l1)

t1 = (1, 2, 3)
print(type(t1))
print(t1[1])

# d1 = {"name": "Yash", "age": 20}

d1 = {"a": 1, "b": 2, "c": 3}
print(type(d1))
print(d1.keys())
print(d1.values())
d1.clear()
print(d1)
d2 = {"x": 10, "y": 20}
d3 = d2.copy()
print(d3)
keys = ["name", "age", "city"]
d4 = dict.fromkeys(keys, "unknown")
print(d4)
d5 = {"name": "Alice", "age": 25}
print(d5.get("name"))
print(d5.get("salary", 0))
print(list(d5.items()))
print(list(d5.keys()))
print(list(d5.values()))
age = d5.pop("age")
print(age)
print(d5)
d6 = {"a": 1, "b": 2, "c": 3}
item = d6.popitem()
print(item)
print(d6)
d7 = {"name": "Bob"}
d7.setdefault("age", 30)
d7.setdefault("name", "Robert")
print(d7)
d8 = {"a": 1, "b": 2}
d8.update({"b": 3, "c": 4})
print(d8)


set1 = {1, 2, 3, 3, 4}
print(type(set1))
print(set1)