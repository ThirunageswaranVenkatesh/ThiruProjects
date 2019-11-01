def TOH(n, from_rod, to_rod, aux_rod):
    #print("1",n,from_rod, to_rod, aux_rod)
    if n == 1:
        #print("2", n,from_rod, to_rod, aux_rod)
        l=len(from_rod)
        top=from_rod[l-1]
        from_rod.pop()
        to_rod.append(top)
        print("A:", A)
        print("B:", B)
        print("C:", C)
        print("\n")
        return
    #print("3", n,from_rod, to_rod, aux_rod)
    TOH(n - 1, from_rod, aux_rod, to_rod)
    #print("4", n,from_rod, to_rod, aux_rod)
    l = len(from_rod)
    top = from_rod[l - 1]
    from_rod.pop()
    to_rod.append(top)
    print("A:", A)
    print("B:", B)
    print("C:", C)
    print("\n")
    TOH(n - 1, aux_rod, to_rod, from_rod)
    #print("5", n,from_rod, to_rod, aux_rod)

A=[3,2,1]
B=[]
C=[]
n = len(A)

print("Initial A:",A)
print("Initial B:",B)
print("Initial C:",C)
print("\n")r
TOH(n,A,C,B)
print("Final A:",A)
print("Final B:",B)
print("Final C:",C)
print("\n")