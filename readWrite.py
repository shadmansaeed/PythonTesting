file = open('test.txt')
# read all the contents
# read n number of characters by passing parameter
# print(file.read())
# print(file.read(2))

# print(file.readline())  # read one single line

# print(file.readline())
#while line!="":
  #  print(line)
   # line = file.readline()


for line in file.readlines():   # values= [abc, cat, dog, fog]
    print(line)

file.close()