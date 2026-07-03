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

d1 = {"name": "Yash", "age": 20}
print(type(d1))
print(d1.keys())
print(d1.values())

set1 = {1, 2, 3, 3, 4}
print(type(set1))
print(set1)