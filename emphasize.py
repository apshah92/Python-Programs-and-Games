def repeat(word,number):

    
    vowel=('a','e','i','o','u','A','E','I','O','U') # you can also take list if you want
    if word[0] in vowel :
         return word

    elif word[1] in vowel and word[2] in vowel: #we don't need to check for word[0]
        return word                             #as we already did in first case
        
        
        

    elif word[2] in vowel:
        word=word.lower()
        newword=''
        for i in range(0,number):
            newword=newword + word[0:3]
        newword=newword + word[3:]
        return newword
    
    elif word[1] in vowel:
        word=word.lower()
        newword=''
        for i in range(0,number):
            newword=newword + word[0:2]
        newword=newword + word[2:]
        return newword

str="Argo"
emphasize=repeat(str,3)
print emphasize

        
        
        
    

