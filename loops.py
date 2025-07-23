greetings = "Good Morning"

a = 4

if a>2:                                             #greetings == "Morning":
    print("Condition matches")
    print("second line")

else:
    print("Condition do not match")

print("If else condition code is completed")

# for loop

obj= [2, 3, 5, 7, 9]

for i in obj:
    print(i*2)
print("End of the calculation")



# sum of First natural numbers 1+2+3+4+5 = 15
# range(i,j) --> i to j-1

summation = 0
for j in range(1, 6):
    summation = summation + j
print("summation is", summation)

print("***********************************")

for k in range(1, 11, 3):
    print(k)


print("********Skipping first index*************")
for m in range(10):
    print(m)
