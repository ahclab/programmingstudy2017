import sys

x = int(sys.argv[1])

filename = sys.argv[2]
my_file = open(filename,"r")

for line in my_file:
    print(int(line)+x)

    
