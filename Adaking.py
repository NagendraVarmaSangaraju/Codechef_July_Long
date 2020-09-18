t = int(input())
for i in range(t):
    n= int(input())
    # m = [[] * 8 for i in range(8)]
    Matrix = [["X" for x in range(8)] for y in range(8)]
   # print(Matrix)
    count = 1
    
    Matrix[0][0] = "O"
    
    for i in range(0,8):
        for j in range(0,8):
            if(i==j and i==0):
                count=count+1
                continue
            elif(count<=n):
                Matrix[i][j]="."
                count=count+1
            
    for row in Matrix:
        print(''.join([str(elem) for elem in row]))
