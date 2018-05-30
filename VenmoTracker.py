def networth(transactions):
    person=[]
    person_cash_flow=[]
    individual_net=0
    all_accounts=[]

    for each in transactions:
        particular_transaction=each.split(':')
        
        name=particular_transaction[0]
        if name not in person:
            person.append(name)
            
        name=particular_transaction[1]
        if name not in person:
            person.append(name)
        
    person.sort()

    for individual in person:
        individual_net=0        
        for each in transactions:
            particular_transaction=each.split(':')
            if individual in particular_transaction:
                if individual==particular_transaction[0]:
                    individual_net=individual_net - float(particular_transaction[2])
                else:
                    individual_net=individual_net + float(particular_transaction[2])
                    
        person_cash_flow.append(str(individual_net))

    for i in range(0,len(person)):
        all_accounts.append(person[i]+':'+person_cash_flow[i])

    return all_accounts

transactions = ["adam:eve:123"]

print "each one's net worth:",networth(transactions)
        
