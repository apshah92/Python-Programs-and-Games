def nameDonor(contributions):
    contributions.sort()
    names=[]
    amounts=[]

    for each in contributions:
        temp=each.split(':')
        if temp[0] not in names:
            names.append(temp[0])

    names.sort()
    print names
    donors_dictionary=dict.fromkeys(names,0)
    print donors_dictionary

    for each in contributions:
        temp=each.split(':')
        name=temp[0]
        amount=float(temp[1])
        donors_dictionary[name]=donors_dictionary[name]+amount
        
    
    most_generous_donor=''
    max_amount=0

    for item in donors_dictionary.items():
        if item[1]>max_amount:
            most_generous_donor=item[0]
            max_amount=item[1]
            

    
    
    return most_generous_donor
            
    

data=["French:30.00","Zack:10.00", "Tie:20.00", "Zack:10.00", "Mack:20.00", 
"Zack:10.00", "Green:10.00", "Zack:10.00", "Mack:10.00","French:10.00"]
print "the most genreous donor is:",nameDonor(data)
            
        
