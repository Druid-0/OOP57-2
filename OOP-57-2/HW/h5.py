def uppercase(func):

    def wrapper():
        return func().upper()
    return wrapper


@uppercase
def say_h():
    return "helloworld"

print(say_h())


