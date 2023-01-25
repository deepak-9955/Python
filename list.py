my_list_1 = [34, 56, 78, 90, 11, 23]
my_list_2 = [None] * len(my_list_1)

for i in range(0, len(my_list_1)):
   my_list_2[i] = my_list_1[i]

print("The list is : ")
for i in range(0, len(my_list_1)):
    print(my_list_1[i])

print()

print("The new list : ")
for i in range(0, len(my_list_2)):
   print(my_list_2[i])