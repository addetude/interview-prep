class Solution(object):
    def matrixReshape(self, mat, r, c):
        if len(mat[0])*len(mat) != r*c:
            return mat
        
        bigList = []
        for li in mat:
            while li:
                bigList.append(li.pop(0))
        
        newList = []
        while bigList:
            temp = []
            for i in range(c):
                temp.append(bigList.pop(0))
            newList.append(temp)
        
        return newList


        return bigList
            


        