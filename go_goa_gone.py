class Solution():
    def __init__(self):
        self.answer=0
        
    
    def planTrip(self, moneyDistributed,numPairs,coldWarMembers):
        #write the solution here. 
        x = moneyDistributed
        go = [[0]*10 for _ in range(10)]
        #print(go)
        M = numPairs
        conflict = coldWarMembers
        for i in conflict:
            go[i[0]-1][i[1]-1] = 1
            go[i[1]-1][i[0]-1] = 1
            
        for i in range(1,(1<<8)-1):
            good = 1
            for j in range(0, 8):
                if (i & (1 << j))>0:
                    for k in range(0,8):
                        if (i & (1 << k))>0:
                            if go[j][k]==1:
                                good = 0
            if good==1:
                s = 0
                for j in range(0,8):
                    if (i & (1 << j))>0:
                        s += x[j]
                        
                self.answer = max(self.answer, s)
        return self.answer
            





if __name__ == "__main__":
    moneyDistributed = list(map(int, input().split()))
    numPairs = int(input())
    coldWarMembers = []
    for i in range(numPairs):
        coldWarMembers.append(tuple(int(x.strip()) for x in input().split(' ')))

    obj = Solution()
    print(obj.planTrip(moneyDistributed, numPairs, coldWarMembers))

