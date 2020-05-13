def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)

    return int(ret)

num = 9119
print ("num was: ")
print(num)

res = square_digits(num)
print("now num is ")
print(res)