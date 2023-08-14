

my_list = ['a', 'a', 'a', 2, 3, 'a', 3, 'a', 2, 4, 9 , 3, 3]
my_set = set(my_list)
# print(my_set)

items = dict()
for i in my_set:
    count_i = my_list.count(i)
    items[i] = count_i

print(max(items, key=items.get))