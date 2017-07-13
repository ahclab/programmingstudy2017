my_list1 = [0,1,2,3,4]
my_list2 = [0,"1",3.0]

print(my_list1[2])
print(my_list2[1])

print("length:%d" % (len(my_list1)))

my_list1.append(8)

print("length:%d" % (len(my_list1)))

for x in my_list1:
    print x
