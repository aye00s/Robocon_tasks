# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        L = []

        while (list1 is not None):
            L.append(list1.val)
            list1 = list1.next

        while (list2 is not None):
            L.append(list2.val)
            list2 = list2.next

        for i in range(len(L)):
            for j in range(0, len(L) - i - 1):
                if L[j] > L[j + 1]:
                    temp = L[j]
                    L[j] = L[j + 1]
                    L[j + 1] = temp

        if len(L) != 0:
            result = ListNode(L[0])
        else:
            return list1

        temp = result
        for i in range(1, len(L)):
            result.next = ListNode(L[i])
            result = result.next

        return temp