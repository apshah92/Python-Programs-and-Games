def freqs(data):
    sorted_data=data
    sorted_data.sort()
    current_word=''
    frequency_list=[]
    frequency=0

    for each in sorted_data:
        if current_word!=each:
            current_word=each
            frequency=sorted_data.count(current_word)
            frequency_list.append(frequency)
    return frequency_list


data = ["a","a","a"]

print "frequency of each word alphabetically ordered:",freqs(data)
            
            
            
            
        
    
