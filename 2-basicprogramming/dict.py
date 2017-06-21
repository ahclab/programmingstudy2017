my_dict = {"orange": 5, "apple": 2}
print(my_dict)
my_dict["lemon"] = 3
print(my_dict["orange"])

if "orange" in my_dict:
    print("There are oranges")
    
for x, y in sorted(my_dict.items()):
    print("%s : %r" % (x,y))

my_list = ["orange","orange","apple"]
for x in my_list:
    my_dict[x] += 1
print(my_dict)

