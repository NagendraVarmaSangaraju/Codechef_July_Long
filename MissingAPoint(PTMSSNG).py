t = int(input())
for i in range(t):
    o=[]
    m=[]
    n= int(input())
    for j in range(4*n-1):
        a, b = map(int, input().split(' '))
        o.append(a)
        m.append(b)
    # print(o, m)
    # print(set(o),set(m))
    # r1= 2 * sum(set(o)) - sum(o) 
    # #r1 = [x for x in o if o.count(x) == 1]
    # r2= 2 * sum(set(m)) - sum(m)
    # #r2 = [x for x in m if m.count(x) == 1]
    # print (r1, r2)
    
    res = o[0] 
    # Do XOR of all elements and return 
    for i in range(1,len(o)): 
        res = res ^ o[i] 
    
        
    res1 = m[0]
    # Do XOR of all elements and return 
    for i in range(1,len(m)): 
        res1 = res1 ^ m[i]    
        
    print (res, res1)
