def modify(name):
    
    a= name.split()
    newname=''
    
    if len(a)==1:
        return name
    elif len(a)==2:
        newname= a[-1]+', '+a[0]
        return newname
    
    else:
        newname=a[-1]+', '+a[0]
        for i in range(1,len(a)-1):
            if len(a[i])==1:
                newname=newname+' '+a[i][0]
            else:
                newname=newname+' '+a[i][0]+'.'
                    
    
    
        
    return newname

nam= 'john A smith '
nam= modify(nam)

print nam
