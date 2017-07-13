import sys
from collections import defaultdict

filename = sys.argv[1]
my_file = open(filename, "r")
my_dict = defaultdict(lambda: 0)

for line in my_file:
    words = line.split(" ")
    for word in words:
        my_dict[word] += 1

for x, y in sorted(my_dict.items()):
    print("%s : %r" % (x,y))
                
