# cook your dish here

n = int(input())
for i in range(n):
    s = int(input())
    m = list(map(int, input().split()))
    #print (m)
    summ= 0
    for j in range(len(m)-1):
        if (m[j+1]-m[j]>0):
            summ= summ+(m[j+1]-m[j])-1
            #print(summ)
        else:
            summ = summ+ m[j]-m[j+1] -1 
            #print(summ)
    print (summ)
