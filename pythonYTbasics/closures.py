# Nested functions
def pop(list):
    def get_last_element():
        return list[len(list) - 1]

    list.remove(get_last_element())


a = [6, 4, 7, 5, 3]
pop(a)
print(a)


# Closure  b keeps ka inner-function after outer-function getting deleted
def outerfunc(text):
    def innerfunc():
        print(text)

    return innerfunc


b = outerfunc('hello world!')
del outerfunc
b()


# making general functions using closure
def nth_power(exponent):
    def pow_of(base):
        return pow(base, exponent)
    return pow_of


square = nth_power(2)
print(square(7))

cube = nth_power(3)
print(cube(5))
