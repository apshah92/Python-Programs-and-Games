def findLabel(labels,deeds,needs):

    badge='nobadge'

    for particular in needs:
        counter=0
        required=particular.split()
        for i in required:
            if i in deeds:
                counter+=1
        if counter==len(required):
            badge=labels[needs.index(particular)]
            break

    return badge

labels = ['first', 'second', 'third', 'fourth']
deeds = ['code', 'talk', 'plan', 'run']
needs = ['code talk plan think', 'talk plan run ', 'plan run code think', 'run code talk think']


print "acc data badge earned:",findLabel(labels,deeds,needs)

        
        
