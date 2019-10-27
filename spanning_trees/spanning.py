class FirstSolution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        if(len(edges)) < 1:
            return [0]
        dic = {}
        for edge in edges:
            if edge[0] not in dic:
                dic[edge[0]] = {}
            dic[edge[0]][edge[1]] = edge[1]
            if edge[1] not in dic:
                dic[edge[1]] = {}
            dic[edge[1]][edge[0]] = edge[0]

        seen = []
        
        def change(dic,curr,pastSeen,last):
            for item in pastSeen:
                if item not in dic[curr]:
                    dic[curr][item] = last
        
        def inform(dic,curr,pastSeen,last):
            if last!=-1:
                change(dic,curr,pastSeen,last)
            pastSeen.append(curr)
            for item in dic[curr]:
                if item != last and item!=curr and item == dic[curr][item]:
                    inform(dic,item,pastSeen,curr)
                    
        #inform(dic,1,seen,-1)
        for i in range(0,N):
            seen = []
            inform(dic,i,seen,-1)
        
        def getDist(dic,currNode,currDist,target):
            if currNode == target:
                return currDist
            return getDist(dic,dic[currNode][target],currDist+1,target)
        
        accs = []
        for i in range(0,N):
            acc = 0
            for j in [x for x in range(0,N) if x != i]:
                acc += getDist(dic,i,0,j)
            accs.append(acc)
        return accs

class SecondSolution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        if(len(edges)) < 1:
            return [0]
        dic = {}
        for edge in edges:
            if edge[0] not in dic:
                dic[edge[0]] = {}
            dic[edge[0]][edge[1]] = edge[1]
            if edge[1] not in dic:
                dic[edge[1]] = {}
            dic[edge[1]][edge[0]] = edge[0]

        seen = []
        
        def change(dic,curr,pastSeen,last):
            for item in pastSeen:
                if item not in dic[curr]:
                    dic[curr][item] = last
        
        def inform(dic,curr,pastSeen,last):
            if last!=-1:
                change(dic,curr,pastSeen,last)
            pastSeen.append(curr)
            for item in dic[curr]:
                if item != last and item!=curr and item == dic[curr][item]:
                    inform(dic,item,pastSeen,curr)
                    
        #inform(dic,1,seen,-1)
        for i in range(0,N):
            seen = []
            inform(dic,i,seen,-1)
        
        def getDist(dic,currNode,currDist,target,start,dists,combos):
            dists[start][currNode] = currDist
            dists[currNode][start] = currDist
            #print(dists[currNode][start])
            combos.discard((start,currNode))
            combos.discard((currNode,start))
            if currNode == target:
                return currDist     #deprecated
            return getDist(dic,dic[currNode][target],currDist+1,target,start,dists,combos)
        


        dists = {}
        combos = set()
        for i in range(0,N):
            dists[i] = {}
            for j in [x for x in range(0,N) if x != i]:
                combos.add((i,j))
                dists[i][j] = -1
                

        while combos:
            item = combos.pop()
            getDist(dic,item[0],0,item[1],item[0],dists,combos)
        
        

        accs = []
        for start in dists:
            acc = 0
            for target in dists[start]:
                acc+=dists[start][target]
            accs.append(acc)
            
        return accs