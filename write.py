# read the file and store the lines in list
# reverse the list
# write the list back to file
with open('test.txt', 'r') as reader:
    content = reader.readlines()   # [arose,bag,cat, dog, elephant, fog]
    reversed(content)              # [fog, elephant, dog, cat,bag]
    with open('test.txt', 'w') as writer:
        for line in reversed(content):

            writer.write(line)

