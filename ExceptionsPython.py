ItemsInCart = 0
# 2 items will be added to cart
if ItemsInCart !=2:
    pass

    #raise Exception("Products Cart count not matching")

assert (ItemsInCart == 0)

# try, catch

try:  # customize message is there is error
    with open('test.txt', 'r') as reader:
        reader.read()
except:

    print("somehow i reached this block because there is failure in try block")


try:   # what python actually through the error
    with open('test.txt', 'r') as reader:
        reader.read()
except Exception as e:

    print(e)

finally:
    print("cleaning up resources")
