class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        i = 0
        slices = 0
        while i < len(A)-1:
            diff = A[i+1] - A[i]
            j = i+1
            while j < len(A):
                ndif = A[j] - A[j-1]
                if ndif != diff:
                    break
                j+=1
            slices += (((j-i-2)**2) + (j-i-2))//2 #compute the triangle number of j-i-2
            i = j-1
        return slices

a = Solution()
print(a.numberOfArithmeticSlices([1, 2, 3, 4,5]))


