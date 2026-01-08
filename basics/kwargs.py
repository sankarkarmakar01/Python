def kwargs_fun(**kwargs):
    print(kwargs)

dict1 = {
    "name":"Sankar",
    "age":21
}

kwargs_fun(name="Sankar",age=21)
kwargs_fun(**dict1)

def demo(*args, **kwargs):
    print(args)
    print(kwargs)

demo(1, 2, 3, name="Rahul", age=22)


def create_user(**data):
    for key, value in data.items():
        print(f"{key} : {value}")

create_user(username="admin", role="manager", active=True)
