class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        A = list(s)
        d = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        check = False
        if len(s) % 2 == 1:
            return False

        if len(s) == 0:
            return True

        if A.count("(") != A.count(")") or A.count("[") != A.count("]") or A.count("{") != A.count("}"):
            return False

        if s[len(s) - 1] in list("{[(") or s[0] in list(")}]"):
            return False

        for i in range(len(s)):

            if s[i] in list("{(["):
                A.insert(0, s[i])


            elif len(A) != 0:
                if s[i] != d.get(A[0]):
                    return False
                elif s[i] == d[A[0]]:
                    check = True
                    del A[0]

            else:
                continue

        return check



