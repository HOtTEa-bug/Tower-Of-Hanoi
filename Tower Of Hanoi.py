#TowerOfHanoi
A = [3,2,1] #SOURCE
B=[] #AUXILLIARY
C=[] #TARGET

def move(n, source, target , auxilliary):
    if n>0:
        move(n-1, source , auxilliary, target)

        target.append(source.pop())
        print ("Move disk",n,"from source",source,"to destination",target)

        print(A, C, B, '#########', sep='\n')

        move(n-1, auxilliary, target, source)



move(3, A, B, C)        

