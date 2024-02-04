class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        L = [0, 0]
        for i in moves:
            if i == "R":
                L[0] += 1
            elif i == "L":
                L[0] -= 1
            elif i == "U":
                L[1] += 1
            elif i == "D":
                L[1] -= 1

        if L == [0, 0]:
            return True
        else:
            return False

