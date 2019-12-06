class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        res = []
        qs = set()
        rows,cols = 0,0
        attackRange = set()
        for queen in queens:
            qs.add(tuple(queen))
            rows = max(rows,queen[0])
            cols = max(cols,queen[1])
        #topleft = [king[0]-min(king),king[1]-min(king)]
        #botleft = [king[0]-min(king),king[1]+min(king)]

        rows = max(rows,king[0])
        cols = max(cols,king[1])
        rows+=1
        cols+=1


        #go to the top left
        dcenter = [king[0],king[1]]
        while dcenter[0] >= 0 and dcenter[1] >= 0:
            if (dcenter[0],dcenter[1]) in qs:
                res.append([dcenter[0],dcenter[1]])
                break
            else:
                dcenter[0]-=1
                dcenter[1]-=1

        #go to the bottom left
        dcenter = [king[0],king[1]]
        while dcenter[0] < rows and dcenter[1] >= 0:
            if (dcenter[0],dcenter[1]) in qs:
                res.append([dcenter[0],dcenter[1]])
                break
            else:
                dcenter[0]+=1
                dcenter[1]-=1

        #go to the top right
        dcenter = [king[0],king[1]]
        while dcenter[0] >= 0 and dcenter[1] < cols:
            if (dcenter[0],dcenter[1]) in qs:
                res.append([dcenter[0],dcenter[1]])
                break
            else:
                dcenter[0]-=1
                dcenter[1]+=1

        #go to the bottom left
        dcenter = [king[0],king[1]]
        while dcenter[0] < rows and dcenter[1] < cols:
            if (dcenter[0],dcenter[1]) in qs:
                res.append([dcenter[0],dcenter[1]])
                break
            else:
                dcenter[0]+=1
                dcenter[1]+=1



        dcenter = [king[0],king[1]]
        while dcenter[1] < cols:
            if (dcenter[0],dcenter[1]) in qs:
                res.append([dcenter[0],dcenter[1]])
                break
            else:
                dcenter[1]+=1

        dcenter = [king[0],king[1]]
        while dcenter[1] >= 0:
            if (dcenter[0],dcenter[1]) in qs:
                res.append([dcenter[0],dcenter[1]])
                break
            else:
                dcenter[1]-=1

        dcenter = [king[0],king[1]]
        while dcenter[0] < rows:
            if (dcenter[0],dcenter[1]) in qs:
                res.append([dcenter[0],dcenter[1]])
                break
            else:
                dcenter[0]+=1

        dcenter = [king[0],king[1]]
        while dcenter[0] >= 0:
            if (dcenter[0],dcenter[1]) in qs:
                res.append([dcenter[0],dcenter[1]])
                break
            else:
                dcenter[0]-=1
        return res


queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]]
king = [3,4]

a = Solution()
print(a.queensAttacktheKing(queens,king))