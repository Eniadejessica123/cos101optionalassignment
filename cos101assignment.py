num_list = [5,98,45,8,5,8,5,8,6,12]

list2 = num_list.copy()

list3 = []

for _ in num_list:
    list3.append(list2[-1])
    list2.pop(-1)

num_list = list3
print(num_list)