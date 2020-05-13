def count_sheeps(sheep):
    # TODO May the force be with you
    count = 0
    for i in sheep:
        if(i):
            count += 1
    return count

array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]

conta = count_sheeps(array1)
print(conta)