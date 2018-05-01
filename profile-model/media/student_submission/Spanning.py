from itertools import combinations
class Spanning():
    def cost(self,g, nodes, threshold):
        a = sum([map(list, combinations(g, i)) for i in range(len(g) + 1)], [])
        b = []
        c = []
        d = []
        d1 = []
        d2 = []
        if nodes >2:
            threshold1 = (nodes-2)*threshold
        else:
            threshold1 = threshold
        for i in a:
            if ( len(i)== nodes-1):
                b.append(i)
        for j in range(0,len(b)):
        
            k = b[j]
            totdis = 0
            for p in range(0,nodes-1):
                m = k[p].split(' ')
                n = int(m[2])
                totdis = totdis + n
            c.append(totdis)
            if ( totdis <= threshold1):
                d.append(j)
        for j in d:
            k1 = b[j]
            totcost = 0
            for p1 in range(0,nodes-1):
                m1 = k1[p1].split(' ')
                n1 = int(m1[3])
                totcost = totcost + n1
            d2.append(totcost)
            
        MIN = min(d2)
        return(MIN)   
       
                  
