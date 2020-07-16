from functools import reduce


# single * for multiple inputs and double ** for multiple key-value pair inputs

def student(name='Default Name', age=5, **marks):
    print('Name : ', name)
    print('Age : ', age)
    for key, value in marks.items():
        print(key, value)


student("Punit", 22, Physics=70, Maths=60, Chemistry=65)

# lamda function

square = lambda x: x * x
sumofthree = lambda x, y, z: x + y + z

print(square(7))
print(sumofthree(10, 20, 15))

# map function -- used when mapping is required like in a list
list1 = [10, 20, 25, 30]
list2 = [4, 5, 3, 2]
a = map(lambda x, y: x + y, list1, list2)
print(list(a))
# for elm in a:
#     print(elm)

# filter function
b = filter(lambda x: x % 2 == 0, list2)
print(list(b))

# reduce function in functool
c = reduce(lambda x, y: x if x > y else y, list2)
print(c)
