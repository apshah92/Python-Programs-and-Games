def reversecomp(dna):

    complement=''
    reverse_complement=''
    original_string='agtc'
    complement_string='tcag'
    for i in dna:
        index=original_string.index(i)
        complement=complement+complement_string[index]

    for i in range(len(complement)-1,-1,-1):
        reverse_complement=reverse_complement+complement[i]

    return reverse_complement


dna_string='t'

print "reverse complement of t:",reversecomp(dna_string)
        
        
        

    
