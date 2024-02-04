class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        L = list()

        for i in range(1, numRows + 1):
            L.append([1] * i)

        for i in range(1, numRows):
            for j in range(1, i):
                L[i][j] = L[i - 1][j - 1] + L[i - 1][j]

        return L
