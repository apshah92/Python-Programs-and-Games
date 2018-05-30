def ratio(dna):
    l=len(dna)
    count=0
    for i in range(l):
        if dna[i] in ('g','c'):
            count=count+1
    ratio= count/float(l)
    return ratio
    

x='agtc'

y=ratio(x)
print y

