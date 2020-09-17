t = int(input())
for i in range(t):
    r= int(input())
    c,m=0,0
    for j in range(r):
        d = list(map(int,input().split()))
        # print(d)
        d11,d22=0,0
        if (d[0]>=10):
          d1 = list(map(int, str(d[0])))
          for k in range(len(d1)):
              d11= d11+d1[k]
          #print(d11)
          d[0] = d11
        if (d[1]>=10):
           d2 = list(map(int, str(d[1])))
          # print (d2)
           for k in range(len(d2)):
               d22= d22+d2[k]
          # print(d22)
           d[1]= d22
        #print(d)
        if(d[0]>d[1]):
            c= c+1
            #print(m,"m")
        elif(d[1]>d[0]):
            m=m+1
            #print(c,"c")
        else:
            c=c+1
            m=m+1
    #print (m,c)
    # print(i)
    if(m<c):
        print (0,c)
        
    elif(c<m):
        print(1,m)
    
    elif(c==m):
        print(2,c)
