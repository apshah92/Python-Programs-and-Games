def countVisible(trophies):
    left_visible=0
    right_visible=0
    length=len(trophies)
    for i in range(0,length):
        if trophies[i]==max(trophies[0:i+1]) and trophies[0:i+1].count(trophies[i])==1:
            left_visible+=1
    for i in range(length-1,-1,-1):
        if trophies[i]==max(trophies[i:length]) and trophies[i:length].count(trophies[i])==1:
            right_visible+=1

    visible_trohpies=[left_visible,right_visible]

    return visible_trohpies

trophylist=[1,2,5,2,1]
print "visible:",countVisible(trophylist)
