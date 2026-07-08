# num = [1,2,3,4,5]
# res = map(lambda a: a*2,num)
# print(list(res))


# name = ["Yash","Shyam","Vineet",]
# res = map(str.upper,name)
# print(list(res))

# n = [5,4,7,8,9]
# ls = map(lambda a: a*1.18,n)
# print(list(ls))


# filter 

# d = ["Yash","Suraj","Vineet","Vansh"]
# g = filter(lambda a: a.startswith('V'),d)
# print(list(g))


from functools import reduce
num = [10,20,30,40,50]
d= reduce(lambda x,y: x+y,num)
print(d)