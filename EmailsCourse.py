def emailsLargest(courses):
    courses.sort()
    newlist=[]

    for each in courses:
        temp=each.split(':')
        if temp[0] not in newlist:
            newlist.append(temp[0])

    newlist.sort()
    course_dictionary=dict.fromkeys(newlist,'')

    for each in courses:
        temp=each.split(':')
        if temp[0] in course_dictionary:
            course_dictionary[temp[0]]=course_dictionary[temp[0]]+" "+temp[2]
        else:
            course_dictionary[temp[0]]=temp[2]

    peoples_email=''
    key_value_list=course_dictionary.items()

    for item in key_value_list:
        if len(item[1])>len(peoples_email):
            peoples_email=item[1]
    return peoples_email

data=["F1:M:m@duke.edu","F1:GH:gh@duke.edu","F1:SH:sh@duke.edu",
"F1:D:d@duke.edu","F1:EF:ef@duke.edu","F1:BC:bc@duke.edu"] 

print "largest course people:",emailsLargest(data)
        
            
    
