def whosDishonest(club1, club2, club3):
    set1=set(club1) & set(club2)
    set2=set(club2) & set(club3)
    set3=set(club3) & set(club1)    

    dishonestset=set1 | set2 | set3   
    
    dishonestlist=list(dishonestset)
    dishonestlist.sort()
    return dishonestlist



data1=["JAMES","HUGH","HUGH","GEORGE","ELIZABETH","ELIZABETH","HUGH",
"DAVID","ROBERT","DAVID","BOB","BOBBY","PAM","JAMES","JAMES"]

data2=["BOBBY","ROBERT","GEORGE","JAMES","PEG","JAMES","DAVID","JOHN","LIZ",
"SANDRA","GEORGE","JOHN","GEORGE","ELIZABETH","LIZ","JAMES"]
data3=["ROBERT","ROBERT","ROBERT","SANDRA","PAM","BOB","LIZ","GEORGE"]



print "dishonest people:",whosDishonest(data1,data2,data3)
