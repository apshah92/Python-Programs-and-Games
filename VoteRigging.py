def minimumVotes(votes):
    max_element=0
    original_votes=votes[0]
    while True:
        max_element=max(votes)
        if(votes[0]==max_element and votes.count(max_element)==1):
            break
        index_max=votes.index(max_element,1)
        votes[index_max]-=1
        votes[0]+=1

    return (votes[0]-original_votes)


votelist=[8,11,11,9,7,3,4]
print "rigged votes:",minimumVotes(votelist)
        
    
