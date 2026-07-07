# file = open("yash.txt","r")
# file = open("yash.txt","r",encoding='utf-8')
# data = file.read()
# print(data)


# file = open("yash.txt","r")
# data = file.read()
# print(data)
# file.close()


# file = open("yash.txt","a")
# data = file.writelines()
# print(data)
# file.close()

# file = open("yash.txt", "w")
# file.write("This will overwrite everything in the file!")
# file.close()


# file = open("yash.txt", "a")
# file.write("\nThis line will be added to the end of the file.")
# file.close()


# file = open("new_yash_file.txt", "x")
# file.write("I just created a brand new file.")
# file.close()


# file = open("yash.txt", "r+")
# data = file.read() 
# print(data)

# file.write("\nAdding some new data too.")
# file.close()

# file = open("yash.txt", "w+")
# file.write("I erased everything and wrote this.")

# file.seek(0) # Move the cursor back to the start
# print(file.read()) # Now read it
# file.close()


# file = open("yash.txt", "a+")
# file.write("\nAdding more data to the end.")

# file.seek(0) # Move the cursor back to the start to read the whole file
# print(file.read())
# file.close()


# file = open("yash.txt","r+")
# print(file.seek(5))
# file = open("yash.txt","r+")
# print(file.tell())
# file.read(4)
# print(file.tell())
# file.close()

# with open ("yash.txt","r") as file:
#     data = file.read()
#     print(data)

with open("yash.txt","+a") as file:
    data = file.writelines("\nHello this is a new line")
    print(data)