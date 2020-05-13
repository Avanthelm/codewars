def is_valid_walk(walk):
    #determine if walk is valid
    if (walk.count('n') == walk.count('s') and 
    walk.count('e') == walk.count('w') and
    len(walk) == 10):
        return True
    return False



#    My shitty solution :/
#    time = len(walk)
#    pos = [0, 0]
#    for x in walk:
#        if(x == 'n'):
#            pos[0] +=1
#        if(x == 's'):
#            pos[0] -=1
#        if(x == 'e'):
#            pos[1] +=1
#        if(x == 'w'):
#            pos[1] -=1
#
#
#    if(time == 10 and pos[0] == 0 and pos[1] == 0):
#        return True
#    else:
#        return False
    pass

walk = ['e', 'w', 'e', 'w', 'w', 's', 'n', 's', 'e', 'w']
check = is_valid_walk(walk)
print(check)