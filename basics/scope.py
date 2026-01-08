a = 10 # global scope

def fun():
    b = 20 # local scope or block scope
    print(a)
    print(b)

fun()
