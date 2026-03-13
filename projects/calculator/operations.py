def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        print("Not division by zero")
        return None
    else:
        return a / b

def mod(a, b):
    if b == 0:
        print("Not division by zero")
        return None
    else:
        return a % b