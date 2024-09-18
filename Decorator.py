##    Decorator

## Its is used to call the function with the help of the another function argument


def This_is_dec(func):
    def inner_fn():
        print("entering into the inner function")
        func()
        print("thanks for chosing decorator")
    return inner_fn

@This_is_dec ## object illama epadi use pannikalam
def sample_fn():
    print("hello world")

# obj = This_is_dec(sample_fn) // normal way
# obj()

# sample_fn()



