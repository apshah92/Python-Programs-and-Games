def combine(foreground, background):
    combinedlist=[]    
    pixel_list=[]

    for i in range(0,len(foreground)):
        index=i
        pixel_list=foreground[i].split(',')
        if int(pixel_list[1])>( int(pixel_list[0])+int(pixel_list[2]) ):
            combinedlist.append(background[index])
        else:
            combinedlist.append(foreground[index])

    return combinedlist

foreground = ["20,200,20", "30,200,30", "50,190,50", "80,190,80", "0,0,0"]

background = ["0,0,0", "0,0,0", "0,0,0", "0,0,0", "255,255,255"]

print "returned list:",combine(foreground, background)
            
            
    
