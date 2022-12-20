def Remove(tuples):
    a = []
    for t in tuples:        
        if t:
            a.append(t)
    return tuples 
 
# Driver Code
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('',''),()]
print(Remove(tuples))