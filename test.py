import random
my_list = []
for x in range(12000):
    my_list.append(random.randint(1, 6))

print(my_list.count(1))