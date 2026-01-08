# f = open("demo.txt","r")
# print(f.read())

# f = open("demo.txt","a")
# f.write("\nI am a data scientist")
#
# f1 = open("demo.txt","r")
# print(f1.read())
# f.close()
# f1.close()


# with open("demo.txt","w") as f:
#     f.write("Hello, Sankar.\n")

with open("demo.txt", "a") as f:
    f.write("Hello, Sankar.\n")

with open("demo.txt", "r") as f:
    print(f.read())