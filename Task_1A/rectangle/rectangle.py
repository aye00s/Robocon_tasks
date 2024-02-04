class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """

        L = []
        i = 1
        while i * i <= area:
            if area % i == 0:
                L = [area // i, i]
            i = i + 1

        return L

