def add(*args):
    # print(type(args))
    print(args[1])
    sum = 0
    for n in args:
        sum += n
        return sum

add(3,9,4)

def calculate(**kwargs):

calculate(add=3, multiply=5)