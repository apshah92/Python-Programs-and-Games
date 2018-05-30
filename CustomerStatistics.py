def reportDuplicates(names):
    sorted_names=names
    sorted_names.sort()
    repeat_customers=[]
    current_name=''
    NAME_OCCURS=''
    frequency=0

    for each in sorted_names:
        if current_name!=each and sorted_names.count(each)>1 :
            current_name=each
            frequency=sorted_names.count(current_name)
            NAME_OCCURS=current_name+' '+str(frequency)
            repeat_customers.append(NAME_OCCURS)
            
            
    return repeat_customers

names = ["ANDREW", "BILL", "CINDY", "DOH", "ERGH", "FOO", "GOO", "HMPH"]

print "repeating customers are:",reportDuplicates(names)
    
