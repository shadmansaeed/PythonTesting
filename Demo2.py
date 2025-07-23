values = [1, 2, "shadman", 4, 5]

# List is data type that allows multiple values and can be different data types

print(values[0])  # 1

print(values[3])  # 4

print(values[-1])  # 5

print(values[1:3])  # 2 rahul

values.insert(3, "saeed")  # insert value between list

print(values)

values.append("End")  # new value in last

print(values)

values[2] = "SHADMAN"  # updating

del values[0]  #delete index

print(values)

# Tuple  -   Same ad LIST Data type but update is not possible
val = (1, 2, "rezowana", 4.5)

print(val[1])

#val[2] = "REZOWANA"

print(val)


# Dictionary works as key and value. as example, here a is key and 2 is value

dic = {"a": 2, 4: "bcd", "c": "Hello world"}

print(dic[4])

print(dic["c"])

dict= {}

dict["firstname "] = "shadman"

dict["last name"] = "saeed"

dict["gender"] = "male"
print(dict)

print(dict["lastname"])

